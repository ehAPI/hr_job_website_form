from openerp.osv import fields, osv

class Jobs_website(osv.osv):

	_name="jobs"

	_columns = {
		'age':fields.integer('Age'),
		}

Jobs_website()