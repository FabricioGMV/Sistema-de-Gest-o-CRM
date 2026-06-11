from datetime import date, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.clientes_model import db, Cliente
from model.servicos_model import TipoServico, ServicoCliente

servico_blueprint = Blueprint('servico', __name__)


# ── US03: Listar tipos de serviço ────────────────────────────────────────────

@servico_blueprint.route('/tipos-servico')
def listar_tipos():
    tipos = TipoServico.query.all()
    return render_template('tipos_servico.html', tipos=tipos)


# ── US03: Cadastrar tipo de serviço ──────────────────────────────────────────

@servico_blueprint.route('/tipos-servico/novo', methods=['GET', 'POST'])
def novo_tipo():
    if request.method == 'POST':
        nome       = request.form.get('nome', '').strip()
        prazo_dias = request.form.get('prazo_dias', '').strip()
        descricao  = request.form.get('descricao', '').strip()

        if not nome or not prazo_dias:
            flash('Nome e prazo são obrigatórios.', 'error')
            return render_template('form_tipo_servico.html', tipo=None)

        tipo = TipoServico(nome=nome, prazo_dias=int(prazo_dias), descricao=descricao)
        db.session.add(tipo)
        db.session.commit()
        flash('Tipo de serviço cadastrado com sucesso!', 'success')
        return redirect(url_for('servico.listar_tipos'))

    return render_template('form_tipo_servico.html', tipo=None)


# ── US03: Editar tipo de serviço ─────────────────────────────────────────────

@servico_blueprint.route('/tipos-servico/editar/<int:id>', methods=['GET', 'POST'])
def editar_tipo(id):
    tipo = db.session.get(TipoServico, id)

    if request.method == 'POST':
        tipo.nome       = request.form.get('nome', '').strip()
        tipo.prazo_dias = int(request.form.get('prazo_dias', 0))
        tipo.descricao  = request.form.get('descricao', '').strip()
        db.session.commit()
        flash('Tipo de serviço atualizado!', 'success')
        return redirect(url_for('servico.listar_tipos'))

    return render_template('form_tipo_servico.html', tipo=tipo)


# ── US03: Excluir tipo de serviço ────────────────────────────────────────────

@servico_blueprint.route('/tipos-servico/excluir/<int:id>', methods=['POST'])
def excluir_tipo(id):
    tipo = db.session.get(TipoServico, id)
    if tipo.servicos:
        flash('Não é possível excluir: existem serviços vinculados a este tipo.', 'error')
    else:
        db.session.delete(tipo)
        db.session.commit()
        flash('Tipo de serviço excluído.', 'success')
    return redirect(url_for('servico.listar_tipos'))


# ── US04: Vincular serviço a cliente ─────────────────────────────────────────

@servico_blueprint.route('/servicos/novo', methods=['GET', 'POST'])
def novo_servico():
    clientes = Cliente.query.all()
    tipos    = TipoServico.query.all()

    if request.method == 'POST':
        cliente_id      = int(request.form.get('cliente_id'))
        tipo_servico_id = int(request.form.get('tipo_servico_id'))
        data_execucao   = date.fromisoformat(request.form.get('data_execucao'))

        # RN07 - data de execução não pode ser futura
        if data_execucao > date.today():
            flash('A data de execução não pode ser futura (RN07).', 'error')
            return render_template('form_servico.html', clientes=clientes, tipos=tipos)

        tipo = db.session.get(TipoServico, tipo_servico_id)

        # RN06 - vencimento calculado automaticamente
        data_vencimento = data_execucao + timedelta(days=tipo.prazo_dias)

        valor_raw = request.form.get('valor', '').strip()
        valor = float(valor_raw.replace(',', '.')) if valor_raw else None

        servico = ServicoCliente(
            cliente_id      = cliente_id,
            tipo_servico_id = tipo_servico_id,
            data_execucao   = data_execucao,
            data_vencimento = data_vencimento,
            status          = 'Ativo',
            valor           = valor
        )
        db.session.add(servico)
        db.session.commit()
        flash('Serviço vinculado com sucesso!', 'success')
        return redirect(url_for('servico.listar_tipos'))

    return render_template('form_servico.html', clientes=clientes, tipos=tipos)