import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/trials')
def users():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT trial.trial_id, last_refreshed_on, trial.public_title, trial_contact.contact_firstname, trial_contact.contact_lastname, trial_contact.contact_address, trial_contact.contact_email, trial_contact.contact_tel, trial_contact.contact_affiliation, trial_criteria.inclusion_agemin, trial_criteria.inclusion_agemax, trial_criteria.inclusion_gender, trial_criteria.target_size, trial_criteria.countries, trial_criteria.inclusion_criteria, trial_criteria.exclusion_criteria, trial_description.scientific_title, trial_description.acronym, trial_description.primary_sponsor, trial_description.web_address, trial_description.recruitment_status, trial_description.other_records, trial_description.date_enrollment, trial_description.study_type, trial_description.study_design, trial_description.phase, trial_description.conditions, trial_description.intervention, trial_description.primary_outcome, trial_description.retrospective_flag, trial_description.bridging_flag_true_false, trial_description.bridged_type, trial_registration.date_registration, trial_registration.date_registration_3,trial_registration.export_date, trial_registration.source_register, trial_results.results_date_posted, trial_results.results_date_completed, trial_results.results_url_link, trial_results.results_yes_no FROM trial INNER JOIN trial_contact ON trial.trial_id = trial_contact.trial_id INNER JOIN trial_criteria ON trial.trial_id = trial_criteria.trial_id INNER JOIN trial_description ON trial.trial_id = trial_description.trial_id INNER JOIN trial_registration ON trial.trial_id = trial_registration.trial_id INNER JOIN trial_results ON trial.trial_id = trial_results.trial_id")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/trial/<string:id>')
def user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT trial.trial_id, last_refreshed_on, trial.public_title, trial_contact.contact_firstname, trial_contact.contact_lastname, trial_contact.contact_address, trial_contact.contact_email, trial_contact.contact_tel, trial_contact.contact_affiliation, trial_criteria.inclusion_agemin, trial_criteria.inclusion_agemax, trial_criteria.inclusion_gender, trial_criteria.target_size, trial_criteria.countries, trial_criteria.inclusion_criteria, trial_criteria.exclusion_criteria, trial_description.scientific_title, trial_description.acronym, trial_description.primary_sponsor, trial_description.web_address, trial_description.recruitment_status, trial_description.other_records, trial_description.date_enrollment, trial_description.study_type, trial_description.study_design, trial_description.phase, trial_description.conditions, trial_description.intervention, trial_description.primary_outcome, trial_description.retrospective_flag, trial_description.bridging_flag_true_false, trial_description.bridged_type, trial_registration.date_registration, trial_registration.date_registration_3,trial_registration.export_date, trial_registration.source_register, trial_results.results_date_posted, trial_results.results_date_completed, trial_results.results_url_link, trial_results.results_yes_no FROM trial INNER JOIN trial_contact ON trial.trial_id = trial_contact.trial_id INNER JOIN trial_criteria ON trial.trial_id = trial_criteria.trial_id INNER JOIN trial_description ON trial.trial_id = trial_description.trial_id INNER JOIN trial_registration ON trial.trial_id = trial_registration.trial_id INNER JOIN trial_results ON trial.trial_id = trial_results.trial_id WHERE trial.trial_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()