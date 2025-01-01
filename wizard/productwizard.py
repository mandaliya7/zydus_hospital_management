from odoo import models, fields

class ProductSelectionWizard(models.TransientModel):
    _name = 'hospital.product.selection.wizard'  # Correct model name
    _description = 'Hospital Product Selection Wizard'

    product_ids = fields.Many2many('product.product', string='Products', required=True)
    quantity = fields.Integer(string='Quantity', default=1)

    def action_confirm(self):
        """ Action when confirming product selection """
        for wizard in self:
            selected_products = wizard.product_ids
            sale_order = self.env['sale.order'].create({
                'partner_id': self.env.context.get('active_id'),  # Assuming the partner is the active ID
                'order_line': [(0, 0, {
                    'product_id': product.id,
                    'name': product.name,
                    'product_uom_qty': wizard.quantity,
                    'price_unit': product.lst_price,
                }) for product in selected_products],
            })

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'res_id': sale_order.id,
                'view_mode': 'form',
                'target': 'current',
            }

    def action_cancel(self):
        """ Action when cancelling the wizard """
        # The cancel action typically closes the wizard without saving any data
        return {'type': 'ir.actions.act_window_close'}


