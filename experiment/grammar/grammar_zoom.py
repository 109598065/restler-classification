""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_accounts_post_id = dependencies.DynamicVariable("_accounts_post_id")

_accounts__accountId__phone_sip_trunk_trunks_post_sip_trunks_0_id = dependencies.DynamicVariable("_accounts__accountId__phone_sip_trunk_trunks_post_sip_trunks_0_id")

_accounts__accountId__sip_trunk_callout_countries_post_callout_countries_0_id = dependencies.DynamicVariable("_accounts__accountId__sip_trunk_callout_countries_post_callout_countries_0_id")

_accounts__accountId__sip_trunk_internal_numbers_post_internal_numbers_0_id = dependencies.DynamicVariable("_accounts__accountId__sip_trunk_internal_numbers_post_internal_numbers_0_id")

_accounts__accountId__sip_trunk_trunks_post_sip_trunks_0_id = dependencies.DynamicVariable("_accounts__accountId__sip_trunk_trunks_post_sip_trunks_0_id")

_chat_users__userId__channels_post_id = dependencies.DynamicVariable("_chat_users__userId__channels_post_id")

_chat_users__userId__messages_post_id = dependencies.DynamicVariable("_chat_users__userId__messages_post_id")

_groups_post_id = dependencies.DynamicVariable("_groups_post_id")

_h323_devices_post_encryption = dependencies.DynamicVariable("_h323_devices_post_encryption")

_h323_devices_post_id = dependencies.DynamicVariable("_h323_devices_post_id")

_h323_devices_post_ip = dependencies.DynamicVariable("_h323_devices_post_ip")

_h323_devices_post_name = dependencies.DynamicVariable("_h323_devices_post_name")

_h323_devices_post_protocol = dependencies.DynamicVariable("_h323_devices_post_protocol")

_im_chat_messages__message_id__put_message_id = dependencies.DynamicVariable("_im_chat_messages__message_id__put_message_id")

_im_chat_messages__message_id__put_robot_jid = dependencies.DynamicVariable("_im_chat_messages__message_id__put_robot_jid")

_im_chat_messages__message_id__put_user_jid = dependencies.DynamicVariable("_im_chat_messages__message_id__put_user_jid")

_im_groups_post_id = dependencies.DynamicVariable("_im_groups_post_id")

_im_groups_post_search_by_account = dependencies.DynamicVariable("_im_groups_post_search_by_account")

_im_groups_post_search_by_domain = dependencies.DynamicVariable("_im_groups_post_search_by_domain")

_im_groups_post_search_by_ma_account = dependencies.DynamicVariable("_im_groups_post_search_by_ma_account")

_meetings__meetingId__polls_post_id = dependencies.DynamicVariable("_meetings__meetingId__polls_post_id")

_meetings__meetingId__registrants_post_id = dependencies.DynamicVariable("_meetings__meetingId__registrants_post_id")

_phone_auto_receptionists_post_extension_number = dependencies.DynamicVariable("_phone_auto_receptionists_post_extension_number")

_phone_auto_receptionists_post_id = dependencies.DynamicVariable("_phone_auto_receptionists_post_id")

_phone_auto_receptionists_post_name = dependencies.DynamicVariable("_phone_auto_receptionists_post_name")

_phone_blocked_list_post_id = dependencies.DynamicVariable("_phone_blocked_list_post_id")

_phone_call_queues_post_extension_number = dependencies.DynamicVariable("_phone_call_queues_post_extension_number")

_phone_call_queues_post_id = dependencies.DynamicVariable("_phone_call_queues_post_id")

_phone_call_queues_post_name = dependencies.DynamicVariable("_phone_call_queues_post_name")

_phone_call_queues_post_status = dependencies.DynamicVariable("_phone_call_queues_post_status")

_phone_common_area_phones_post_display_name = dependencies.DynamicVariable("_phone_common_area_phones_post_display_name")

_phone_common_area_phones_post_id = dependencies.DynamicVariable("_phone_common_area_phones_post_id")

_phone_setting_templates_post_description = dependencies.DynamicVariable("_phone_setting_templates_post_description")

_phone_setting_templates_post_id = dependencies.DynamicVariable("_phone_setting_templates_post_id")

_phone_setting_templates_post_name = dependencies.DynamicVariable("_phone_setting_templates_post_name")

_phone_sites_post_id = dependencies.DynamicVariable("_phone_sites_post_id")

_phone_sites_post_name = dependencies.DynamicVariable("_phone_sites_post_name")

_phone_users__userId__phone_numbers_post_phone_numbers_0_id = dependencies.DynamicVariable("_phone_users__userId__phone_numbers_post_phone_numbers_0_id")

_rooms_post_id = dependencies.DynamicVariable("_rooms_post_id")

_rooms_post_name = dependencies.DynamicVariable("_rooms_post_name")

_rooms_post_type = dependencies.DynamicVariable("_rooms_post_type")

_rooms_locations_post_id = dependencies.DynamicVariable("_rooms_locations_post_id")

_tracking_fields_post_field = dependencies.DynamicVariable("_tracking_fields_post_field")

_tracking_fields_post_id = dependencies.DynamicVariable("_tracking_fields_post_id")

_tracking_fields_post_recommended_values_0 = dependencies.DynamicVariable("_tracking_fields_post_recommended_values_0")

_tracking_fields_post_required = dependencies.DynamicVariable("_tracking_fields_post_required")

_tracking_fields_post_visible = dependencies.DynamicVariable("_tracking_fields_post_visible")

_users_post_email = dependencies.DynamicVariable("_users_post_email")

_users_post_first_name = dependencies.DynamicVariable("_users_post_first_name")

_users_post_id = dependencies.DynamicVariable("_users_post_id")

_users_post_last_name = dependencies.DynamicVariable("_users_post_last_name")

_users_post_type = dependencies.DynamicVariable("_users_post_type")

_users__userId__meetings_post_agenda = dependencies.DynamicVariable("_users__userId__meetings_post_agenda")

_users__userId__meetings_post_duration = dependencies.DynamicVariable("_users__userId__meetings_post_duration")

_users__userId__meetings_post_id = dependencies.DynamicVariable("_users__userId__meetings_post_id")

_users__userId__meetings_post_password = dependencies.DynamicVariable("_users__userId__meetings_post_password")

_users__userId__meetings_post_start_time = dependencies.DynamicVariable("_users__userId__meetings_post_start_time")

_users__userId__meetings_post_timezone = dependencies.DynamicVariable("_users__userId__meetings_post_timezone")

_users__userId__meetings_post_topic = dependencies.DynamicVariable("_users__userId__meetings_post_topic")

_users__userId__meetings_post_type = dependencies.DynamicVariable("_users__userId__meetings_post_type")

_users__userId__tsp_post_conference_code = dependencies.DynamicVariable("_users__userId__tsp_post_conference_code")

_users__userId__tsp_post_leader_pin = dependencies.DynamicVariable("_users__userId__tsp_post_leader_pin")

_users__userId__tsp_post_tsp_bridge = dependencies.DynamicVariable("_users__userId__tsp_post_tsp_bridge")

_users__userId__webinars_post_agenda = dependencies.DynamicVariable("_users__userId__webinars_post_agenda")

_users__userId__webinars_post_duration = dependencies.DynamicVariable("_users__userId__webinars_post_duration")

_users__userId__webinars_post_password = dependencies.DynamicVariable("_users__userId__webinars_post_password")

_users__userId__webinars_post_start_time = dependencies.DynamicVariable("_users__userId__webinars_post_start_time")

_users__userId__webinars_post_timezone = dependencies.DynamicVariable("_users__userId__webinars_post_timezone")

_users__userId__webinars_post_topic = dependencies.DynamicVariable("_users__userId__webinars_post_topic")

_users__userId__webinars_post_type = dependencies.DynamicVariable("_users__userId__webinars_post_type")

_webinars__webinarId__panelists_post_id = dependencies.DynamicVariable("_webinars__webinarId__panelists_post_id")

_webinars__webinarId__polls_post_id = dependencies.DynamicVariable("_webinars__webinarId__polls_post_id")

_webinars__webinarId__registrants_post_id = dependencies.DynamicVariable("_webinars__webinarId__registrants_post_id")

def parse_accountspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_accounts_post_id", temp_7262)


def parse_accountsaccountIdphonesip_trunktrunkspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8173 = str(data["sip_trunks"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_accounts__accountId__phone_sip_trunk_trunks_post_sip_trunks_0_id", temp_8173)


def parse_accountsaccountIdsip_trunkcallout_countriespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7680 = str(data["callout_countries"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_accounts__accountId__sip_trunk_callout_countries_post_callout_countries_0_id", temp_7680)


def parse_accountsaccountIdsip_trunkinternal_numberspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5581 = str(data["internal_numbers"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_accounts__accountId__sip_trunk_internal_numbers_post_internal_numbers_0_id", temp_5581)


def parse_accountsaccountIdsip_trunktrunkspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2060 = str(data["sip_trunks"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_accounts__accountId__sip_trunk_trunks_post_sip_trunks_0_id", temp_2060)


def parse_chatusersuserIdchannelspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5588 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_chat_users__userId__channels_post_id", temp_5588)


def parse_chatusersuserIdmessagespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9060 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_chat_users__userId__messages_post_id", temp_9060)


def parse_groupspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4421 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4421 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4421:
        dependencies.set_variable("_groups_post_id", temp_4421)


def parse_h323devicespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9775 = None
    temp_2737 = None
    temp_2919 = None
    temp_4673 = None
    temp_6326 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9775 = str(data["encryption"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2737 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2919 = str(data["ip"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4673 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6326 = str(data["protocol"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775 or temp_2737 or temp_2919 or temp_4673 or temp_6326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_h323_devices_post_encryption", temp_9775)
    if temp_2737:
        dependencies.set_variable("_h323_devices_post_id", temp_2737)
    if temp_2919:
        dependencies.set_variable("_h323_devices_post_ip", temp_2919)
    if temp_4673:
        dependencies.set_variable("_h323_devices_post_name", temp_4673)
    if temp_6326:
        dependencies.set_variable("_h323_devices_post_protocol", temp_6326)


def parse_imchatmessagesmessage_idput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4695 = None
    temp_9821 = None
    temp_303 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4695 = str(data["message_id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9821 = str(data["robot_jid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["user_jid"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4695 or temp_9821 or temp_303):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4695:
        dependencies.set_variable("_im_chat_messages__message_id__put_message_id", temp_4695)
    if temp_9821:
        dependencies.set_variable("_im_chat_messages__message_id__put_robot_jid", temp_9821)
    if temp_303:
        dependencies.set_variable("_im_chat_messages__message_id__put_user_jid", temp_303)


def parse_imgroupspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8623 = None
    temp_9953 = None
    temp_6771 = None
    temp_3145 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8623 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9953 = str(data["search_by_account"])
            temp_9953 = temp_9953.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6771 = str(data["search_by_domain"])
            temp_6771 = temp_6771.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3145 = str(data["search_by_ma_account"])
            temp_3145 = temp_3145.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8623 or temp_9953 or temp_6771 or temp_3145):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8623:
        dependencies.set_variable("_im_groups_post_id", temp_8623)
    if temp_9953:
        dependencies.set_variable("_im_groups_post_search_by_account", temp_9953)
    if temp_6771:
        dependencies.set_variable("_im_groups_post_search_by_domain", temp_6771)
    if temp_3145:
        dependencies.set_variable("_im_groups_post_search_by_ma_account", temp_3145)


def parse_meetingsmeetingIdpollspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8169 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8169 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8169):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8169:
        dependencies.set_variable("_meetings__meetingId__polls_post_id", temp_8169)


def parse_meetingsmeetingIdregistrantspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8480 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8480 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8480):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8480:
        dependencies.set_variable("_meetings__meetingId__registrants_post_id", temp_8480)


def parse_phoneauto_receptionistspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9919 = None
    temp_326 = None
    temp_6999 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9919 = str(data["extension_number"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_326 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6999 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9919 or temp_326 or temp_6999):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9919:
        dependencies.set_variable("_phone_auto_receptionists_post_extension_number", temp_9919)
    if temp_326:
        dependencies.set_variable("_phone_auto_receptionists_post_id", temp_326)
    if temp_6999:
        dependencies.set_variable("_phone_auto_receptionists_post_name", temp_6999)


def parse_phoneblocked_listpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5262:
        dependencies.set_variable("_phone_blocked_list_post_id", temp_5262)


def parse_phonecall_queuespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9340 = None
    temp_6876 = None
    temp_5468 = None
    temp_811 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9340 = str(data["extension_number"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6876 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5468 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_811 = str(data["status"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9340 or temp_6876 or temp_5468 or temp_811):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9340:
        dependencies.set_variable("_phone_call_queues_post_extension_number", temp_9340)
    if temp_6876:
        dependencies.set_variable("_phone_call_queues_post_id", temp_6876)
    if temp_5468:
        dependencies.set_variable("_phone_call_queues_post_name", temp_5468)
    if temp_811:
        dependencies.set_variable("_phone_call_queues_post_status", temp_811)


def parse_phonecommon_area_phonespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1871 = None
    temp_4533 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_1871 = str(data["display_name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4533 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1871 or temp_4533):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1871:
        dependencies.set_variable("_phone_common_area_phones_post_display_name", temp_1871)
    if temp_4533:
        dependencies.set_variable("_phone_common_area_phones_post_id", temp_4533)


def parse_phonesetting_templatespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2971 = None
    temp_9885 = None
    temp_6426 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2971 = str(data["description"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9885 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6426 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2971 or temp_9885 or temp_6426):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2971:
        dependencies.set_variable("_phone_setting_templates_post_description", temp_2971)
    if temp_9885:
        dependencies.set_variable("_phone_setting_templates_post_id", temp_9885)
    if temp_6426:
        dependencies.set_variable("_phone_setting_templates_post_name", temp_6426)


def parse_phonesitespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7629 = None
    temp_303 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7629 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7629 or temp_303):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7629:
        dependencies.set_variable("_phone_sites_post_id", temp_7629)
    if temp_303:
        dependencies.set_variable("_phone_sites_post_name", temp_303)


def parse_phoneusersuserIdphone_numberspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_3810 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_3810 = str(data["phone_numbers"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_3810):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_3810:
        dependencies.set_variable("_phone_users__userId__phone_numbers_post_phone_numbers_0_id", temp_3810)


def parse_roomspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_3431 = None
    temp_9574 = None
    temp_5051 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_3431 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9574 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5051 = str(data["type"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_3431 or temp_9574 or temp_5051):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_3431:
        dependencies.set_variable("_rooms_post_id", temp_3431)
    if temp_9574:
        dependencies.set_variable("_rooms_post_name", temp_9574)
    if temp_5051:
        dependencies.set_variable("_rooms_post_type", temp_5051)


def parse_roomslocationspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7159 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7159 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7159):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7159:
        dependencies.set_variable("_rooms_locations_post_id", temp_7159)


def parse_tracking_fieldspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1189 = None
    temp_2734 = None
    temp_9070 = None
    temp_7947 = None
    temp_3371 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_1189 = str(data["field"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2734 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9070 = str(data["recommended_values"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7947 = str(data["required"])
            temp_7947 = temp_7947.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3371 = str(data["visible"])
            temp_3371 = temp_3371.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1189 or temp_2734 or temp_9070 or temp_7947 or temp_3371):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1189:
        dependencies.set_variable("_tracking_fields_post_field", temp_1189)
    if temp_2734:
        dependencies.set_variable("_tracking_fields_post_id", temp_2734)
    if temp_9070:
        dependencies.set_variable("_tracking_fields_post_recommended_values_0", temp_9070)
    if temp_7947:
        dependencies.set_variable("_tracking_fields_post_required", temp_7947)
    if temp_3371:
        dependencies.set_variable("_tracking_fields_post_visible", temp_3371)


def parse_userspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4572 = None
    temp_1468 = None
    temp_2213 = None
    temp_4100 = None
    temp_7187 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4572 = str(data["email"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1468 = str(data["first_name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2213 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4100 = str(data["last_name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7187 = str(data["type"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4572 or temp_1468 or temp_2213 or temp_4100 or temp_7187):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4572:
        dependencies.set_variable("_users_post_email", temp_4572)
    if temp_1468:
        dependencies.set_variable("_users_post_first_name", temp_1468)
    if temp_2213:
        dependencies.set_variable("_users_post_id", temp_2213)
    if temp_4100:
        dependencies.set_variable("_users_post_last_name", temp_4100)
    if temp_7187:
        dependencies.set_variable("_users_post_type", temp_7187)


def parse_usersuserIdmeetingspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6198 = None
    temp_4879 = None
    temp_1949 = None
    temp_8781 = None
    temp_8254 = None
    temp_7353 = None
    temp_8582 = None
    temp_6797 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_6198 = str(data["agenda"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4879 = str(data["duration"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1949 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8781 = str(data["password"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8254 = str(data["start_time"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7353 = str(data["timezone"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8582 = str(data["topic"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6797 = str(data["type"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6198 or temp_4879 or temp_1949 or temp_8781 or temp_8254 or temp_7353 or temp_8582 or temp_6797):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6198:
        dependencies.set_variable("_users__userId__meetings_post_agenda", temp_6198)
    if temp_4879:
        dependencies.set_variable("_users__userId__meetings_post_duration", temp_4879)
    if temp_1949:
        dependencies.set_variable("_users__userId__meetings_post_id", temp_1949)
    if temp_8781:
        dependencies.set_variable("_users__userId__meetings_post_password", temp_8781)
    if temp_8254:
        dependencies.set_variable("_users__userId__meetings_post_start_time", temp_8254)
    if temp_7353:
        dependencies.set_variable("_users__userId__meetings_post_timezone", temp_7353)
    if temp_8582:
        dependencies.set_variable("_users__userId__meetings_post_topic", temp_8582)
    if temp_6797:
        dependencies.set_variable("_users__userId__meetings_post_type", temp_6797)


def parse_usersuserIdtsppost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6248 = None
    temp_2184 = None
    temp_8953 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_6248 = str(data["conference_code"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2184 = str(data["leader_pin"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8953 = str(data["tsp_bridge"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6248 or temp_2184 or temp_8953):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6248:
        dependencies.set_variable("_users__userId__tsp_post_conference_code", temp_6248)
    if temp_2184:
        dependencies.set_variable("_users__userId__tsp_post_leader_pin", temp_2184)
    if temp_8953:
        dependencies.set_variable("_users__userId__tsp_post_tsp_bridge", temp_8953)


def parse_usersuserIdwebinarspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8964 = None
    temp_865 = None
    temp_8385 = None
    temp_1701 = None
    temp_6441 = None
    temp_8268 = None
    temp_2191 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_8964 = str(data["agenda"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_865 = str(data["duration"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8385 = str(data["password"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1701 = str(data["start_time"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6441 = str(data["timezone"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8268 = str(data["topic"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2191 = str(data["type"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8964 or temp_865 or temp_8385 or temp_1701 or temp_6441 or temp_8268 or temp_2191):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8964:
        dependencies.set_variable("_users__userId__webinars_post_agenda", temp_8964)
    if temp_865:
        dependencies.set_variable("_users__userId__webinars_post_duration", temp_865)
    if temp_8385:
        dependencies.set_variable("_users__userId__webinars_post_password", temp_8385)
    if temp_1701:
        dependencies.set_variable("_users__userId__webinars_post_start_time", temp_1701)
    if temp_6441:
        dependencies.set_variable("_users__userId__webinars_post_timezone", temp_6441)
    if temp_8268:
        dependencies.set_variable("_users__userId__webinars_post_topic", temp_8268)
    if temp_2191:
        dependencies.set_variable("_users__userId__webinars_post_type", temp_2191)


def parse_webinarswebinarIdpanelistspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9999 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_9999 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9999):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9999:
        dependencies.set_variable("_webinars__webinarId__panelists_post_id", temp_9999)


def parse_webinarswebinarIdpollspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4813 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_4813 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4813):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4813:
        dependencies.set_variable("_webinars__webinarId__polls_post_id", temp_4813)


def parse_webinarswebinarIdregistrantspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6522 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_6522 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6522):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6522:
        dependencies.set_variable("_webinars__webinarId__registrants_post_id", temp_6522)

req_collection = requests.RequestCollection([])
# Endpoint: /accounts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts"
)
req_collection.add_request(request)

# Endpoint: /accounts, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "account_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "options":
        {
            "billing_auto_renew":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "meeting_connector_list":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "pay_mode":"""),
    primitives.restler_fuzzable_group("pay_mode", ['master','sub'] , default_enum="master" ,quoted=True),
    primitives.restler_static_string(""",
            "room_connector_list":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "share_mc":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "share_rc":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountspost,
            'dependencies':
            [
                _accounts_post_id.writer()
            ]
        }

    },

],
requestId="/accounts"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/billing, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("billing"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/billing"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/billing, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("billing"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "apt":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/billing"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/billing/invoices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("billing"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invoices"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/billing/invoices"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/billing/invoices/{invoiceId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("billing"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invoices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/billing/invoices/{invoiceId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/lock_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lock_settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/lock_settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/lock_settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lock_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/lock_settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/managed_domains, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("managed_domains"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/managed_domains"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/options, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("options"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "billing_auto_renew":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "meeting_connector_list":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "pay_mode":"""),
    primitives.restler_fuzzable_group("pay_mode", ['master','sub'] , default_enum="master" ,quoted=True),
    primitives.restler_static_string(""",
    "room_connector_list":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "share_mc":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "share_rc":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/options"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/owner, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owner"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/owner"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/phone/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "byoc":
        {
            "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/phone/settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/phone/setup, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setup"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "emergency_address":
        {
            "address_line1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "address_line2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "state_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "extension_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/phone/setup"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/phone/sip_trunk/trunks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sip_trunks":
    [
        {
            "carrier_account":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountsaccountIdphonesip_trunktrunkspost,
            'dependencies':
            [
                _accounts__accountId__phone_sip_trunk_trunks_post_sip_trunks_0_id.writer()
            ]
        }

    },

],
requestId="/accounts/{accountId}/phone/sip_trunk/trunks"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/phone/sip_trunk/trunks/{sipTrunkId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts__accountId__phone_sip_trunk_trunks_post_sip_trunks_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "carrier_account":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/phone/sip_trunk/trunks/{sipTrunkId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "contact":
        {
            "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "apt":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "plan_audio":
        {
            "callout_countries":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "ddi_numbers":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "premium_countries":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "tollfree_countries":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "plan_base":
        {
            "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "plan_large_meeting":
    [
        {
            "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_static_string(_users__userId__meetings_post_type.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "plan_phone":
        {
            "plan_base":
                {
                    "callout_countries":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "plan_calling":
            [
                {
                    "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "plan_number":
            [
                {
                    "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "plan_recording":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "plan_room_connector":
        {
            "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "plan_webinar":
    [
        {
            "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_static_string(_users__userId__webinars_post_type.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "plan_zoom_rooms":
        {
            "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_static_string(_rooms_post_type.reader(), quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/addons, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addons"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/addons"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/addons, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addons"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/addons"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/addons/status, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("addons"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['cancel']  ,quoted=True),
    primitives.restler_static_string(""",
    "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reason":"""),
    primitives.restler_fuzzable_group("reason", ['1','2','3','4','5','6']  ,quoted=False),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/addons/status"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/base, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("base"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "hosts":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/base"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/base/status, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("base"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "reason":"""),
    primitives.restler_fuzzable_group("reason", ['1','2','3','4','5','6']  ,quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/base/status"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/plans/usage, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("plans"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("usage"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/plans/usage"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication','security','meeting_security']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/settings/virtual_backgrounds, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/settings/virtual_backgrounds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/callout_countries, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("callout_countries"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/callout_countries"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/callout_countries, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("callout_countries"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "callout_countries":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountsaccountIdsip_trunkcallout_countriespost,
            'dependencies':
            [
                _accounts__accountId__sip_trunk_callout_countries_post_callout_countries_0_id.writer()
            ]
        }

    },

],
requestId="/accounts/{accountId}/sip_trunk/callout_countries"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/callout_countries/{countryId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("callout_countries"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts__accountId__sip_trunk_callout_countries_post_callout_countries_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/callout_countries/{countryId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/internal_numbers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal_numbers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/internal_numbers"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/internal_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "internal_numbers":
    [
        {
            "allow_for_external_meetings":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "allow_join":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "display_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "labels":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "languages":"""),
    primitives.restler_fuzzable_group("languages", ['en-GB','en-US','de-DE']  ,quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1']  ,quoted=False),
    primitives.restler_static_string(""",
            "visible":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountsaccountIdsip_trunkinternal_numberspost,
            'dependencies':
            [
                _accounts__accountId__sip_trunk_internal_numbers_post_internal_numbers_0_id.writer()
            ]
        }

    },

],
requestId="/accounts/{accountId}/sip_trunk/internal_numbers"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/internal_numbers/{numberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal_numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts__accountId__sip_trunk_internal_numbers_post_internal_numbers_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/internal_numbers/{numberId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/numbers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/numbers"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_numbers":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/numbers"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "show_callout_internal_number":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "show_zoom_provided_callout_countries":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "show_zoom_provided_numbers":"""),
    primitives.restler_fuzzable_group("show_zoom_provided_numbers", ['0','1','2']  ,quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/settings"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/trunks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/trunks"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/trunks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sip_trunks":
    [
        {
            "dnis":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "outbound_caller_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_accountsaccountIdsip_trunktrunkspost,
            'dependencies':
            [
                _accounts__accountId__sip_trunk_trunks_post_sip_trunks_0_id.writer()
            ]
        }

    },

],
requestId="/accounts/{accountId}/sip_trunk/trunks"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/sip_trunk/trunks/{trunkId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts__accountId__sip_trunk_trunks_post_sip_trunks_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/sip_trunk/trunks/{trunkId}"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/trusted_domains, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trusted_domains"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/trusted_domains"
)
req_collection.add_request(request)

# Endpoint: /accounts/{accountId}/users/{userId}/account, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accounts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "account_id":"""),
    primitives.restler_static_string(_accounts_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/accounts/{accountId}/users/{userId}/account"
)
req_collection.add_request(request)

# Endpoint: /api/download/billing/invoices/{invoiceId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("billing"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invoices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/download/billing/invoices/{invoiceId}"
)
req_collection.add_request(request)

# Endpoint: /archive_files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive_files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query_data_type="),
    primitives.restler_fuzzable_group("query_data_type", ['meeting_start_time','archive_complete_time'] , default_enum="meeting_start_time" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/archive_files"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}/members/me, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}/members/me"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}/members/me, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}/members/me"
)
req_collection.add_request(request)

# Endpoint: /chat/channels/{channelId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/channels/{channelId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/me/contacts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contacts"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/me/contacts"
)
req_collection.add_request(request)

# Endpoint: /chat/users/me/contacts/{contactId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contacts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query_presence_status="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/me/contacts/{contactId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3']  ,quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_chatusersuserIdchannelspost,
            'dependencies':
            [
                _chat_users__userId__channels_post_id.writer()
            ]
        }

    },

],
requestId="/chat/users/{userId}/channels"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}/members"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}/members"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/channels/{channelId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__channels_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/channels/{channelId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/messages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("to_contact="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to_channel="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("date="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_deleted_and_edited_message="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/messages"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/messages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "at_items":
    [
        {
            "at_contact":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "at_type":"""),
    primitives.restler_fuzzable_group("at_type", ['1','2']  ,quoted=False),
    primitives.restler_static_string(""",
            "end_position":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "start_position":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ],
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "to_channel":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "to_contact":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_chatusersuserIdmessagespost,
            'dependencies':
            [
                _chat_users__userId__messages_post_id.writer()
            ]
        }

    },

],
requestId="/chat/users/{userId}/messages"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/messages/{messageId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__messages_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("to_contact="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to_channel="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/messages/{messageId}"
)
req_collection.add_request(request)

# Endpoint: /chat/users/{userId}/messages/{messageId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_chat_users__userId__messages_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "to_channel":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "to_contact":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/chat/users/{userId}/messages/{messageId}"
)
req_collection.add_request(request)

# Endpoint: /contacts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contacts"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search_key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query_presence_status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/contacts"
)
req_collection.add_request(request)

# Endpoint: /groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups"
)
req_collection.add_request(request)

# Endpoint: /groups, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_groupspost,
            'dependencies':
            [
                _groups_post_id.writer()
            ]
        }

    },

],
requestId="/groups"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/lock_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lock_settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/lock_settings"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/lock_settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lock_settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/lock_settings"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/members"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/members"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/members/{memberId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['move','set_primary']  ,quoted=True),
    primitives.restler_static_string(""",
    "target_group_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/settings"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication','meeting_security']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/settings"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/settings/virtual_backgrounds, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /groups/{groupId}/settings/virtual_backgrounds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/groups/{groupId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /h323/devices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("h323"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/h323/devices"
)
req_collection.add_request(request)

# Endpoint: /h323/devices, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("h323"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "encryption":"""),
    primitives.restler_fuzzable_group("encryption", ['auto','yes','no']  ,quoted=True),
    primitives.restler_static_string(""",
    "ip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "protocol":"""),
    primitives.restler_fuzzable_group("protocol", ['H.323','SIP']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_h323devicespost,
            'dependencies':
            [
                _h323_devices_post_encryption.writer(),
                _h323_devices_post_id.writer(),
                _h323_devices_post_ip.writer(),
                _h323_devices_post_name.writer(),
                _h323_devices_post_protocol.writer()
            ]
        }

    },

],
requestId="/h323/devices"
)
req_collection.add_request(request)

# Endpoint: /h323/devices/{deviceId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("h323"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_h323_devices_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/h323/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /h323/devices/{deviceId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("h323"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_h323_devices_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "encryption":"""),
    primitives.restler_static_string(_h323_devices_post_encryption.reader(), quoted=True),
    primitives.restler_static_string(""",
    "ip":"""),
    primitives.restler_static_string(_h323_devices_post_ip.reader(), quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_h323_devices_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "protocol":"""),
    primitives.restler_static_string(_h323_devices_post_protocol.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/h323/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /im/chat/messages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "content":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "is_markdown_support":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "robot_jid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "to_jid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "user_jid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "visible_to_user":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/chat/messages"
)
req_collection.add_request(request)

# Endpoint: /im/chat/messages/{message_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_chat_messages__message_id__put_message_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "robot_jid":"""),
    primitives.restler_static_string(_im_chat_messages__message_id__put_robot_jid.reader(), quoted=True),
    primitives.restler_static_string(""",
    "user_jid":"""),
    primitives.restler_static_string(_im_chat_messages__message_id__put_user_jid.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/chat/messages/{message_id}"
)
req_collection.add_request(request)

# Endpoint: /im/chat/messages/{message_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("message_id"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "account_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "content":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "is_markdown_support":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "robot_jid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "user_jid":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_imchatmessagesmessage_idput,
            'dependencies':
            [
                _im_chat_messages__message_id__put_message_id.writer(),
                _im_chat_messages__message_id__put_robot_jid.writer(),
                _im_chat_messages__message_id__put_user_jid.writer()
            ]
        }

    },

],
requestId="/im/chat/messages/{message_id}"
)
req_collection.add_request(request)

# Endpoint: /im/chat/sessions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/chat/sessions"
)
req_collection.add_request(request)

# Endpoint: /im/chat/sessions/{sessionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sessions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/chat/sessions/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /im/groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups"
)
req_collection.add_request(request)

# Endpoint: /im/groups, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "search_by_account":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "search_by_domain":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "search_by_ma_account":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_group("type", ['normal','shared','restricted'] , default_enum="normal" ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_imgroupspost,
            'dependencies':
            [
                _im_groups_post_id.writer(),
                _im_groups_post_search_by_account.writer(),
                _im_groups_post_search_by_domain.writer(),
                _im_groups_post_search_by_ma_account.writer()
            ]
        }

    },

],
requestId="/im/groups"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "search_by_account":"""),
    primitives.restler_static_string(_im_groups_post_search_by_account.reader(), quoted=False),
    primitives.restler_static_string(""",
    "search_by_domain":"""),
    primitives.restler_static_string(_im_groups_post_search_by_domain.reader(), quoted=False),
    primitives.restler_static_string(""",
    "search_by_ma_account":"""),
    primitives.restler_static_string(_im_groups_post_search_by_ma_account.reader(), quoted=False),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_group("type", ['normal','shared','restricted']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}/members"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}/members"
)
req_collection.add_request(request)

# Endpoint: /im/groups/{groupId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_im_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/groups/{groupId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /im/users/me/chat/messages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("chat_user="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/users/me/chat/messages"
)
req_collection.add_request(request)

# Endpoint: /im/users/{userId}/chat/messages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chat"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("chat_user="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("channel="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/im/users/{userId}/chat/messages"
)
req_collection.add_request(request)

# Endpoint: /live_meetings/{meetingId}/events, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("live_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/live_meetings/{meetingId}/events"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule_for_reminder="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cancel_meeting_reminder="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("show_previous_occurrences="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "schedule_for":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "agenda":"""),
    primitives.restler_static_string(_users__userId__meetings_post_agenda.reader(), quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_static_string(_users__userId__meetings_post_duration.reader(), quoted=False),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_static_string(_users__userId__meetings_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
    "recurrence":
        {
            "end_date_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "end_times":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_day":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_week":"""),
    primitives.restler_fuzzable_group("monthly_week", ['-1','1','2','3','4']  ,quoted=False),
    primitives.restler_static_string(""",
            "monthly_week_day":"""),
    primitives.restler_fuzzable_group("monthly_week_day", ['1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string(""",
            "repeat_interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3']  ,quoted=False),
    primitives.restler_static_string(""",
            "weekly_days":"""),
    primitives.restler_fuzzable_group("weekly_days", ['1','2','3','4','5','6','7'] , default_enum="1" ,quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "settings":
        {
            "allow_multiple_devices":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "alternative_hosts":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "alternative_hosts_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "approval_type":"""),
    primitives.restler_fuzzable_group("approval_type", ['0','1','2'] , default_enum="2" ,quoted=False),
    primitives.restler_static_string(""",
            "approved_or_denied_countries_or_regions":
                {
                    "approved_list":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "denied_list":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "method":"""),
    primitives.restler_fuzzable_group("method", ['approve','deny']  ,quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "audio":"""),
    primitives.restler_fuzzable_group("audio", ['both','telephony','voip'] , default_enum="both" ,quoted=True),
    primitives.restler_static_string(""",
            "authentication_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_exception":
            [
                {
                    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "authentication_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_option":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "auto_recording":"""),
    primitives.restler_fuzzable_group("auto_recording", ['local','cloud','none'] , default_enum="none" ,quoted=True),
    primitives.restler_static_string(""",
            "breakout_room":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "rooms":
                    [
                        {
                            "name":"""),
    primitives.restler_static_string(_rooms_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "participants":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ]
                }
            ,
            "close_registration":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "cn_meeting":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "contact_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "contact_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "custom_keys":
            [
                {
                    "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "encryption_type":"""),
    primitives.restler_fuzzable_group("encryption_type", ['enhanced_encryption','e2ee']  ,quoted=True),
    primitives.restler_static_string(""",
            "enforce_login":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "enforce_login_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "global_dial_in_countries":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "global_dial_in_numbers":
            [
                {
                    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "country_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['toll','tollfree']  ,quoted=True),
    primitives.restler_static_string("""
                }
            ],
            "host_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "in_meeting":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "jbh_time":"""),
    primitives.restler_fuzzable_group("jbh_time", ['0','5','10']  ,quoted=False),
    primitives.restler_static_string(""",
            "join_before_host":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "language_interpretation":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "interpreters":
                    [
                        {
                            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "languages":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ]
                }
            ,
            "meeting_authentication":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "mute_upon_entry":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "participant_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_confirmation_email":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registration_type":"""),
    primitives.restler_fuzzable_group("registration_type", ['1','2','3'] , default_enum="1" ,quoted=False),
    primitives.restler_static_string(""",
            "show_share_button":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "use_pmi":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "waiting_room":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "watermark":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_confirmation_email":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "start_time":"""),
    primitives.restler_static_string(_users__userId__meetings_post_start_time.reader(), quoted=True),
    primitives.restler_static_string(""",
    "template_id":"""),
    primitives.restler_static_string(_users__userId__meetings_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_static_string(_users__userId__meetings_post_timezone.reader(), quoted=True),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_static_string(_users__userId__meetings_post_topic.reader(), quoted=True),
    primitives.restler_static_string(""",
    "tracking_fields":
    [
        {
            "field":"""),
    primitives.restler_static_string(_tracking_fields_post_field.reader(), quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_static_string(_users__userId__meetings_post_type.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/batch_polls, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("batch_polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/batch_polls"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/invitation, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("invitation"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/invitation"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/livestream, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livestream"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/livestream"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/livestream, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livestream"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "page_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "stream_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "stream_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/livestream"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/livestream/status, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("livestream"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['start','stop']  ,quoted=True),
    primitives.restler_static_string(""",
    "settings":
        {
            "active_speaker_name":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/livestream/status"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/polls"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/polls, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_meetingsmeetingIdpollspost,
            'dependencies':
            [
                _meetings__meetingId__polls_post_id.writer()
            ]
        }

    },

],
requestId="/meetings/{meetingId}/polls"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/polls/{pollId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_meetings__meetingId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/polls/{pollId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_meetings__meetingId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/polls/{pollId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_meetings__meetingId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("action="),
    primitives.restler_fuzzable_group("action", ['trash','delete'] , default_enum="trash" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ttl="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/registrants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['pending','approved','denied'] , default_enum="approved" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/registrants"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/registrants, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "comments":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "custom_questions":
    [
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "industry":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "job_title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "no_of_employees":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "org":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "purchasing_time_frame":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role_in_purchase_process":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/registrants"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/registrants/questions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/registrants/questions, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "custom_questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['short','single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "questions":
    [
        {
            "field_name":"""),
    primitives.restler_fuzzable_group("field_name", ['last_name','address','city','country','zip','state','phone','industry','org','job_title','purchasing_time_frame','role_in_purchase_process','no_of_employees','comments']  ,quoted=True),
    primitives.restler_static_string(""",
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/registrants/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['approve','deny']  ,quoted=True),
    primitives.restler_static_string(""",
    "registrants":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/registrants/status"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/settings"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "approval_type":"""),
    primitives.restler_fuzzable_group("approval_type", ['0','1','2']  ,quoted=False),
    primitives.restler_static_string(""",
    "authentication_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "authentication_option":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "on_demand":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "recording_authentication":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "send_email_to_host":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "share_recording":"""),
    primitives.restler_fuzzable_group("share_recording", ['publicly','internally','none']  ,quoted=True),
    primitives.restler_static_string(""",
    "show_social_share_buttons":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "viewer_download":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/settings"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/status"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/{recordingId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("action="),
    primitives.restler_fuzzable_group("action", ['trash','delete'] , default_enum="trash" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/{recordingId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/recordings/{recordingId}/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/recordings/{recordingId}/status"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['pending','approved','denied'] , default_enum="approved" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/registrants"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "comments":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "custom_questions":
    [
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "industry":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "job_title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "no_of_employees":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "org":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "purchasing_time_frame":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role_in_purchase_process":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "auto_approve":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_meetingsmeetingIdregistrantspost,
            'dependencies':
            [
                _meetings__meetingId__registrants_post_id.writer()
            ]
        }

    },

],
requestId="/meetings/{meetingId}/registrants"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants/questions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants/questions, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "custom_questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['short','single']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "questions":
    [
        {
            "field_name":"""),
    primitives.restler_fuzzable_group("field_name", ['address','city','country','zip','state','phone','industry','org','job_title','purchasing_time_frame','role_in_purchase_process','no_of_employees','comments']  ,quoted=True),
    primitives.restler_static_string(""",
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['approve','cancel','deny']  ,quoted=True),
    primitives.restler_static_string(""",
    "registrants":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/registrants/status"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/registrants/{registrantId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_meetings__meetingId__registrants_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/registrants/{registrantId}"
)
req_collection.add_request(request)

# Endpoint: /meetings/{meetingId}/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['end','recover']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/meetings/{meetingId}/status"
)
req_collection.add_request(request)

# Endpoint: /metrics/client/feedback, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("feedback"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/client/feedback"
)
req_collection.add_request(request)

# Endpoint: /metrics/client/feedback/{feedbackId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("feedback"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/client/feedback/{feedbackId}"
)
req_collection.add_request(request)

# Endpoint: /metrics/client/satisfaction, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("satisfaction"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/client/satisfaction"
)
req_collection.add_request(request)

# Endpoint: /metrics/crc, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("crc"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/crc"
)
req_collection.add_request(request)

# Endpoint: /metrics/im, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("im"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/im"
)
req_collection.add_request(request)

# Endpoint: /metrics/issues/zoomrooms, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zoomrooms"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/issues/zoomrooms"
)
req_collection.add_request(request)

# Endpoint: /metrics/issues/zoomrooms/{zoomroomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zoomrooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/issues/zoomrooms/{zoomroomId}"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_group("include_fields", ['tracking_fields']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_group("include_fields", ['registrant_id']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}/participants"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}/participants/qos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}/participants/qos"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}/participants/satisfaction, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("satisfaction"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}/participants/satisfaction"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}/participants/sharing, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sharing"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}/participants/sharing"
)
req_collection.add_request(request)

# Endpoint: /metrics/meetings/{meetingId}/participants/{participantId}/qos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/meetings/{meetingId}/participants/{participantId}/qos"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_group("include_fields", ['registrant_id']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}/participants"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}/participants/qos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}/participants/qos"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}/participants/satisfaction, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("satisfaction"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}/participants/satisfaction"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}/participants/sharing, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sharing"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}/participants/sharing"
)
req_collection.add_request(request)

# Endpoint: /metrics/webinars/{webinarId}/participants/{participantId}/qos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','live'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/webinars/{webinarId}/participants/{participantId}/qos"
)
req_collection.add_request(request)

# Endpoint: /metrics/zoomrooms, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zoomrooms"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/zoomrooms"
)
req_collection.add_request(request)

# Endpoint: /metrics/zoomrooms/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zoomrooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/zoomrooms/issues"
)
req_collection.add_request(request)

# Endpoint: /metrics/zoomrooms/{zoomroomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zoomrooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/metrics/zoomrooms/{zoomroomId}"
)
req_collection.add_request(request)

# Endpoint: /past_meetings/{meetingId}/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_meetings/{meetingId}/files"
)
req_collection.add_request(request)

# Endpoint: /past_meetings/{meetingId}/instances, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("instances"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_meetings/{meetingId}/instances"
)
req_collection.add_request(request)

# Endpoint: /past_meetings/{meetingId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_meetings/{meetingId}/polls"
)
req_collection.add_request(request)

# Endpoint: /past_meetings/{meetingUUID}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_meetings/{meetingUUID}"
)
req_collection.add_request(request)

# Endpoint: /past_meetings/{meetingUUID}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_meetings/{meetingUUID}/participants"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{WebinarUUID}/absentees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("absentees"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{WebinarUUID}/absentees"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{webinarId}/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{webinarId}/files"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{webinarId}/instances, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("instances"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{webinarId}/instances"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{webinarId}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{webinarId}/participants"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{webinarId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{webinarId}/polls"
)
req_collection.add_request(request)

# Endpoint: /past_webinars/{webinarId}/qa, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("past_webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qa"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/past_webinars/{webinarId}/qa"
)
req_collection.add_request(request)

# Endpoint: /phone/auto_receptionists, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auto_receptionists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phoneauto_receptionistspost,
            'dependencies':
            [
                _phone_auto_receptionists_post_extension_number.writer(),
                _phone_auto_receptionists_post_id.writer(),
                _phone_auto_receptionists_post_name.writer()
            ]
        }

    },

],
requestId="/phone/auto_receptionists"
)
req_collection.add_request(request)

# Endpoint: /phone/auto_receptionists/{autoReceptionistId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auto_receptionists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_auto_receptionists_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "extension_number":"""),
    primitives.restler_static_string(_phone_auto_receptionists_post_extension_number.reader(), quoted=False),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_phone_auto_receptionists_post_name.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/auto_receptionists/{autoReceptionistId}"
)
req_collection.add_request(request)

# Endpoint: /phone/auto_receptionists/{autoReceptionistId}/phone_numbers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auto_receptionists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_auto_receptionists_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/auto_receptionists/{autoReceptionistId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/auto_receptionists/{autoReceptionistId}/phone_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auto_receptionists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_auto_receptionists_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_numbers":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/auto_receptionists/{autoReceptionistId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/auto_receptionists/{autoReceptionistId}/phone_numbers/{phoneNumberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("auto_receptionists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_auto_receptionists_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/auto_receptionists/{autoReceptionistId}/phone_numbers/{phoneNumberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/blocked_list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocked_list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/blocked_list"
)
req_collection.add_request(request)

# Endpoint: /phone/blocked_list, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocked_list"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "block_type":"""),
    primitives.restler_fuzzable_group("block_type", ['inbound','outbound']  ,quoted=True),
    primitives.restler_static_string(""",
    "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "match_type":"""),
    primitives.restler_fuzzable_group("match_type", ['phoneNumber','prefix']  ,quoted=True),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_group("status", ['active','inactive']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phoneblocked_listpost,
            'dependencies':
            [
                _phone_blocked_list_post_id.writer()
            ]
        }

    },

],
requestId="/phone/blocked_list"
)
req_collection.add_request(request)

# Endpoint: /phone/blocked_list/{blockedListId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocked_list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_blocked_list_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/blocked_list/{blockedListId}"
)
req_collection.add_request(request)

# Endpoint: /phone/blocked_list/{blockedListId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocked_list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_blocked_list_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/blocked_list/{blockedListId}"
)
req_collection.add_request(request)

# Endpoint: /phone/blocked_list/{blockedListId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blocked_list"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_blocked_list_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "block_type":"""),
    primitives.restler_fuzzable_group("block_type", ['inbound','outbound']  ,quoted=True),
    primitives.restler_static_string(""",
    "comment":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "match_type":"""),
    primitives.restler_fuzzable_group("match_type", ['phoneNumber','prefix']  ,quoted=True),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_group("status", ['active','inactive']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/blocked_list/{blockedListId}"
)
req_collection.add_request(request)

# Endpoint: /phone/byoc_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("byoc_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "carrier":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone_numbers":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/byoc_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/call_logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("time_type="),
    primitives.restler_fuzzable_group("time_type", ['startTime','endTime'] , default_enum="startTime" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_logs"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "members":
        {
            "common_area_phone_ids":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "users":
            [
                {
                    "email":"""),
    primitives.restler_static_string(_users_post_email.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phonecall_queuespost,
            'dependencies':
            [
                _phone_call_queues_post_extension_number.writer(),
                _phone_call_queues_post_id.writer(),
                _phone_call_queues_post_name.writer(),
                _phone_call_queues_post_status.writer()
            ]
        }

    },

],
requestId="/phone/call_queues"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_static_string(_phone_call_queues_post_extension_number.reader(), quoted=False),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_phone_call_queues_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_static_string(_phone_call_queues_post_status.reader(), quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/manager, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("manager"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "member_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/manager"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/members, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/members"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
        {
            "common_area_phone_ids":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "users":
            [
                {
                    "email":"""),
    primitives.restler_static_string(_users_post_email.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/members"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/phone_numbers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/phone_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_numbers":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/phone_numbers/{phoneNumberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/phone_numbers/{phoneNumberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/call_queues/{callQueueId}/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_queues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_call_queues_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/call_queues/{callQueueId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /phone/calling_plans, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calling_plans"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/calling_plans"
)
req_collection.add_request(request)

# Endpoint: /phone/common_area_phones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("common_area_phones"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/common_area_phones"
)
req_collection.add_request(request)

# Endpoint: /phone/common_area_phones, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("common_area_phones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "mac_address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "model":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "time_zone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phonecommon_area_phonespost,
            'dependencies':
            [
                _phone_common_area_phones_post_display_name.writer(),
                _phone_common_area_phones_post_id.writer()
            ]
        }

    },

],
requestId="/phone/common_area_phones"
)
req_collection.add_request(request)

# Endpoint: /phone/common_area_phones/{commonAreaPhoneId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("common_area_phones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_common_area_phones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/common_area_phones/{commonAreaPhoneId}"
)
req_collection.add_request(request)

# Endpoint: /phone/common_area_phones/{commonAreaPhoneId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("common_area_phones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_common_area_phones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/common_area_phones/{commonAreaPhoneId}"
)
req_collection.add_request(request)

# Endpoint: /phone/common_area_phones/{commonAreaPhoneId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("common_area_phones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_common_area_phones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "display_name":"""),
    primitives.restler_static_string(_phone_common_area_phones_post_display_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "mac_address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_static_string(_phone_common_area_phones_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/common_area_phones/{commonAreaPhoneId}"
)
req_collection.add_request(request)

# Endpoint: /phone/company_number, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("company_number"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/company_number"
)
req_collection.add_request(request)

# Endpoint: /phone/devices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['assigned','unassigned']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/devices"
)
req_collection.add_request(request)

# Endpoint: /phone/devices, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assigned_to":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "display_name":"""),
    primitives.restler_static_string(_h323_devices_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "mac_address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "model":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/devices"
)
req_collection.add_request(request)

# Endpoint: /phone/devices/{deviceId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /phone/devices/{deviceId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /phone/devices/{deviceId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assigned_to":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "display_name":"""),
    primitives.restler_static_string(_h323_devices_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "mac_address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/devices/{deviceId}"
)
req_collection.add_request(request)

# Endpoint: /phone/metrics/call_logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quality_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/metrics/call_logs"
)
req_collection.add_request(request)

# Endpoint: /phone/metrics/call_logs/{callId}/qos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/metrics/call_logs/{callId}/qos"
)
req_collection.add_request(request)

# Endpoint: /phone/metrics/call_logs/{call_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("metrics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/metrics/call_logs/{call_id}"
)
req_collection.add_request(request)

# Endpoint: /phone/numbers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['assigned','unassigned','all']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("extension_type="),
    primitives.restler_fuzzable_group("extension_type", ['user','callQueue','autoReceptionist','commonAreaPhone']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("number_type="),
    primitives.restler_fuzzable_group("number_type", ['toll','tollfree']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pending_numbers="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/numbers/{numberId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/numbers/{numberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/numbers/{numberId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "capability":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/numbers/{numberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("owner_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recording_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/recordings"
)
req_collection.add_request(request)

# Endpoint: /phone/reports/operationlogs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reports"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operationlogs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/reports/operationlogs"
)
req_collection.add_request(request)

# Endpoint: /phone/setting_templates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting_templates"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/setting_templates"
)
req_collection.add_request(request)

# Endpoint: /phone/setting_templates, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting_templates"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_group("type", ['user','group','autoReceptionist','commonarea','interop']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phonesetting_templatespost,
            'dependencies':
            [
                _phone_setting_templates_post_description.writer(),
                _phone_setting_templates_post_id.writer(),
                _phone_setting_templates_post_name.writer()
            ]
        }

    },

],
requestId="/phone/setting_templates"
)
req_collection.add_request(request)

# Endpoint: /phone/setting_templates/{templateId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting_templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_setting_templates_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/setting_templates/{templateId}"
)
req_collection.add_request(request)

# Endpoint: /phone/setting_templates/{templateId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting_templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_setting_templates_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_static_string(_phone_setting_templates_post_description.reader(), quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_phone_setting_templates_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "policy":
        {
            "ad_hoc_call_recording":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "recording_start_prompt":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "recording_transcription":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
            ,
            "auto_call_recording":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "recording_calls":"""),
    primitives.restler_fuzzable_group("recording_calls", ['inbound','outbound','both']  ,quoted=True),
    primitives.restler_static_string(""",
                    "recording_start_prompt":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "recording_transcription":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
            ,
            "sms":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "international_sms":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
            ,
            "voicemail":
                {
                    "allow_transcription":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
        }
    ,
    "profile":
        {
            "area_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "user_settings":
        {
            "audio_prompt_language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "block_calls_without_caller_id":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "call_handling":
                {
                    "business_hours":
                        {
                            "business_hour_action":"""),
    primitives.restler_fuzzable_group("business_hour_action", ['0','1','9','26','50']  ,quoted=False),
    primitives.restler_static_string(""",
                            "connect_to_operator":
                                {
                                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                                    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "type":"""),
    primitives.restler_fuzzable_group("type", ['user','zoomRoom','commonAreaPhone','autoReceptionist','callQueue','sharedLineGroup']  ,quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "custom_hours":
                            [
                                {
                                    "from":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "to":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2']  ,quoted=False),
    primitives.restler_static_string(""",
                                    "weekday":"""),
    primitives.restler_fuzzable_group("weekday", ['1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                                }
                            ],
                            "ring_type":"""),
    primitives.restler_fuzzable_group("ring_type", ['0','1']  ,quoted=True),
    primitives.restler_static_string(""",
                            "ringing_duration":"""),
    primitives.restler_fuzzable_group("ringing_duration", ['15','20','25','30','35','40','45','50','55','60']  ,quoted=True),
    primitives.restler_static_string(""",
                            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2']  ,quoted=False),
    primitives.restler_static_string("""
                        }
                    ,
                    "close_hours":
                        {
                            "close_hour_action":"""),
    primitives.restler_fuzzable_group("close_hour_action", ['0','1','9','26','50']  ,quoted=False),
    primitives.restler_static_string(""",
                            "connect_to_operator":
                                {
                                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                                    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                                    "type":"""),
    primitives.restler_fuzzable_group("type", ['user','zoomRoom','commonAreaPhone','autoReceptionist','callQueue','sharedLineGroup']  ,quoted=True),
    primitives.restler_static_string("""
                                }
                            ,
                            "max_wait_time":"""),
    primitives.restler_fuzzable_group("max_wait_time", ['15','20','25','30','35','40','45','50','55','60']  ,quoted=True),
    primitives.restler_static_string("""
                        }
                }
            ,
            "desk_phone":
                {
                    "pin_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "hold_music":"""),
    primitives.restler_fuzzable_group("hold_music", ['default','disable']  ,quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/setting_templates/{templateId}"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "display_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "extension_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "primary_number":
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "status":"""),
    primitives.restler_fuzzable_group("status", ['active','inactive']  ,quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}/members, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}/members"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
        {
            "common_area_phone_ids":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "users":
            [
                {
                    "email":"""),
    primitives.restler_static_string(_users_post_email.reader(), quoted=True),
    primitives.restler_static_string(""",
                    "id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string("""
                }
            ]
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}/members"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_numbers":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/shared_line_groups/{sharedLineGroupId}/phone_numbers/{phoneNumberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("shared_line_groups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/shared_line_groups/{sharedLineGroupId}/phone_numbers/{phoneNumberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/sip_trunk/trunks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trunks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/sip_trunk/trunks"
)
req_collection.add_request(request)

# Endpoint: /phone/sites, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sites"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/sites"
)
req_collection.add_request(request)

# Endpoint: /phone/sites, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sites"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auto_receptionist_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "default_emergency_address":
        {
            "address_line1":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "address_line2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "state_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "short_extension":
        {
            "length":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "site_code":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phonesitespost,
            'dependencies':
            [
                _phone_sites_post_id.writer(),
                _phone_sites_post_name.writer()
            ]
        }

    },

],
requestId="/phone/sites"
)
req_collection.add_request(request)

# Endpoint: /phone/sites/{siteId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sites"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_sites_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("transfer_site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/sites/{siteId}"
)
req_collection.add_request(request)

# Endpoint: /phone/sites/{siteId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sites"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_sites_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/sites/{siteId}"
)
req_collection.add_request(request)

# Endpoint: /phone/sites/{siteId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sites"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_sites_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_static_string(_phone_sites_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "site_code":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/sites/{siteId}"
)
req_collection.add_request(request)

# Endpoint: /phone/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("site_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "extension_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "site_id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/call_logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','missed']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("phone_number="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("time_type="),
    primitives.restler_fuzzable_group("time_type", ['startTime','endTime'] , default_enum="startTime" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/call_logs"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/call_logs/{callLogId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("call_logs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/call_logs/{callLogId}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/calling_plans, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calling_plans"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "calling_plans":
    [
        {
            "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/calling_plans"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/calling_plans/{type}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("calling_plans"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/calling_plans/{type}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/phone_numbers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "phone_numbers":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_phoneusersuserIdphone_numberspost,
            'dependencies':
            [
                _phone_users__userId__phone_numbers_post_phone_numbers_0_id.writer()
            ]
        }

    },

],
requestId="/phone/users/{userId}/phone_numbers"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/phone_numbers/{phoneNumberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone_numbers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_phone_users__userId__phone_numbers_post_phone_numbers_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/phone_numbers/{phoneNumberId}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/settings"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/settings/{settingType}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("shared_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/settings/{settingType}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/settings/{settingType}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "voice_mail":
        {
            "access_user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "delete":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "download":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "shared_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/settings/{settingType}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/settings/{settingType}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "voice_mail":
        {
            "access_user_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "delete":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "download":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/settings/{settingType}"
)
req_collection.add_request(request)

# Endpoint: /phone/users/{userId}/voice_mails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("voice_mails"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['all','read','unread'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/users/{userId}/voice_mails"
)
req_collection.add_request(request)

# Endpoint: /phone/voice_mails/{voicemailId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("phone"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("voice_mails"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/phone/voice_mails/{voicemailId}"
)
req_collection.add_request(request)

# Endpoint: /report/activities, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activities"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/activities"
)
req_collection.add_request(request)

# Endpoint: /report/cloud_recording, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cloud_recording"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/cloud_recording"
)
req_collection.add_request(request)

# Endpoint: /report/daily, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("daily"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("year="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("month="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/daily"
)
req_collection.add_request(request)

# Endpoint: /report/meetings/{meetingId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/meetings/{meetingId}"
)
req_collection.add_request(request)

# Endpoint: /report/meetings/{meetingId}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_group("include_fields", ['registrant_id']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/meetings/{meetingId}/participants"
)
req_collection.add_request(request)

# Endpoint: /report/meetings/{meetingId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/meetings/{meetingId}/polls"
)
req_collection.add_request(request)

# Endpoint: /report/operationlogs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operationlogs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category_type="),
    primitives.restler_fuzzable_group("category_type", ['all','user','user_settings','account','billing','im','recording','phone_contacts','webinar','sub_account','role','zoom_rooms']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/operationlogs"
)
req_collection.add_request(request)

# Endpoint: /report/telephone, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("telephone"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['1','3'] , default_enum="1" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/telephone"
)
req_collection.add_request(request)

# Endpoint: /report/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['active','inactive']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/users"
)
req_collection.add_request(request)

# Endpoint: /report/users/{userId}/meetings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['past','pastOne'] , default_enum="past" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/users/{userId}/meetings"
)
req_collection.add_request(request)

# Endpoint: /report/webinars/{webinarId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/webinars/{webinarId}"
)
req_collection.add_request(request)

# Endpoint: /report/webinars/{webinarId}/participants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("participants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_group("include_fields", ['registrant_id']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/webinars/{webinarId}/participants"
)
req_collection.add_request(request)

# Endpoint: /report/webinars/{webinarId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/webinars/{webinarId}/polls"
)
req_collection.add_request(request)

# Endpoint: /report/webinars/{webinarId}/qa, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("qa"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/report/webinars/{webinarId}/qa"
)
req_collection.add_request(request)

# Endpoint: /roles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles"
)
req_collection.add_request(request)

# Endpoint: /roles, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "privileges":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "privileges":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "sub_account_privileges":
        {
            "second_level":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
        }
    ,
    "total_members":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_count="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}/members"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "members":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}/members"
)
req_collection.add_request(request)

# Endpoint: /roles/{roleId}/members/{memberId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("roles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/roles/{roleId}/members/{memberId}"
)
req_collection.add_request(request)

# Endpoint: /rooms, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['Offline','Available','InMeeting','UnderConstruction']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['ZoomRoom','SchedulingDisplayOnly','DigitalSignageOnly']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("unassigned_rooms="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("location_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms"
)
req_collection.add_request(request)

# Endpoint: /rooms, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "location_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_group("type", ['ZoomRoom','SchedulingDisplayOnly','DigitalSignageOnly']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_roomspost,
            'dependencies':
            [
                _rooms_post_id.writer(),
                _rooms_post_name.writer(),
                _rooms_post_type.writer()
            ]
        }

    },

],
requestId="/rooms"
)
req_collection.add_request(request)

# Endpoint: /rooms/account_profile, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_profile"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/account_profile"
)
req_collection.add_request(request)

# Endpoint: /rooms/account_profile, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_profile"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "basic":
        {
            "required_code_to_ext":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "room_passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/account_profile"
)
req_collection.add_request(request)

# Endpoint: /rooms/account_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_group("setting_type", ['meeting','alert'] , default_enum="meeting" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/account_settings"
)
req_collection.add_request(request)

# Endpoint: /rooms/account_settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("account_settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/account_settings"
)
req_collection.add_request(request)

# Endpoint: /rooms/digital_signage, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("digital_signage"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("folder_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/digital_signage"
)
req_collection.add_request(request)

# Endpoint: /rooms/events, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/events"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("parent_location_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "parent_location_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_roomslocationspost,
            'dependencies':
            [
                _rooms_locations_post_id.writer()
            ]
        }

    },

],
requestId="/rooms/locations"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/structure, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("structure"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/structure"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/structure, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("structure"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "structures":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/structure"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/{locationId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/{locationId}"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/{locationId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "basic":
        {
            "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "description ":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "required_code_to_ext":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "room_passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/{locationId}"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/{locationId}/location, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("location"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "parent_location_id":"""),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/{locationId}/location"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/{locationId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/{locationId}/settings"
)
req_collection.add_request(request)

# Endpoint: /rooms/locations/{locationId}/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/locations/{locationId}/settings"
)
req_collection.add_request(request)

# Endpoint: /rooms/{id}/events, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "method":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "params":
        {
            "calendar_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "change_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "event_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "resource_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{id}/events"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "basic":
        {
            "hide_room_in_contacts":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "required_code_to_ext":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "room_passcode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "support_phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}/devices, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}/devices"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}/devices/{deviceId}/app_version, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("devices"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("app_version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['upgrade','downgrade','cancel']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}/devices/{deviceId}/app_version"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}/location, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("location"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "location_id":"""),
    primitives.restler_static_string(_rooms_locations_post_id.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}/location"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}/settings"
)
req_collection.add_request(request)

# Endpoint: /rooms/{roomId}/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_rooms_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("setting_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/rooms/{roomId}/settings"
)
req_collection.add_request(request)

# Endpoint: /sip_phones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_phones"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search_key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/sip_phones"
)
req_collection.add_request(request)

# Endpoint: /sip_phones, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_phones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "authorization_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "domain":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server3":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server3":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "registration_expire_time":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "transport_protocol":"""),
    primitives.restler_fuzzable_group("transport_protocol", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "transport_protocol2":"""),
    primitives.restler_fuzzable_group("transport_protocol2", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "transport_protocol3":"""),
    primitives.restler_fuzzable_group("transport_protocol3", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "user_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "user_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "voice_mail":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/sip_phones"
)
req_collection.add_request(request)

# Endpoint: /sip_phones/{phoneId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_phones"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/sip_phones/{phoneId}"
)
req_collection.add_request(request)

# Endpoint: /sip_phones/{phoneId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_phones"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "authorization_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "domain":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "proxy_server3":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server2":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "register_server3":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "registration_expire_time":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "transport_protocol":"""),
    primitives.restler_fuzzable_group("transport_protocol", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "transport_protocol2":"""),
    primitives.restler_fuzzable_group("transport_protocol2", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "transport_protocol3":"""),
    primitives.restler_fuzzable_group("transport_protocol3", ['UDP','TCP','TLS','AUTO']  ,quoted=True),
    primitives.restler_static_string(""",
    "user_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "voice_mail":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/sip_phones/{phoneId}"
)
req_collection.add_request(request)

# Endpoint: /sip_trunk/numbers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sip_trunk"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("numbers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/sip_trunk/numbers"
)
req_collection.add_request(request)

# Endpoint: /tracking_fields, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_fields"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tracking_fields"
)
req_collection.add_request(request)

# Endpoint: /tracking_fields, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_fields"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "field":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "recommended_values":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "visible":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_tracking_fieldspost,
            'dependencies':
            [
                _tracking_fields_post_field.writer(),
                _tracking_fields_post_id.writer(),
                _tracking_fields_post_recommended_values_0.writer(),
                _tracking_fields_post_required.writer(),
                _tracking_fields_post_visible.writer()
            ]
        }

    },

],
requestId="/tracking_fields"
)
req_collection.add_request(request)

# Endpoint: /tracking_fields/{fieldId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_fields"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_tracking_fields_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tracking_fields/{fieldId}"
)
req_collection.add_request(request)

# Endpoint: /tracking_fields/{fieldId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_fields"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_tracking_fields_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tracking_fields/{fieldId}"
)
req_collection.add_request(request)

# Endpoint: /tracking_fields/{fieldId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_fields"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_tracking_fields_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "field":"""),
    primitives.restler_static_string(_tracking_fields_post_field.reader(), quoted=True),
    primitives.restler_static_string(""",
    "recommended_values":"""),
    primitives.restler_static_string(_tracking_fields_post_recommended_values_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "required":"""),
    primitives.restler_static_string(_tracking_fields_post_required.reader(), quoted=False),
    primitives.restler_static_string(""",
    "visible":"""),
    primitives.restler_static_string(_tracking_fields_post_visible.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tracking_fields/{fieldId}"
)
req_collection.add_request(request)

# Endpoint: /tsp, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tsp"
)
req_collection.add_request(request)

# Endpoint: /tsp, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "dial_in_number_unrestricted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "master_account_setting_extended":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "modify_credential_forbidden":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "tsp_bridge":"""),
    primitives.restler_static_string(_users__userId__tsp_post_tsp_bridge.reader(), quoted=True),
    primitives.restler_static_string(""",
    "tsp_enabled":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "tsp_provider":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/tsp"
)
req_collection.add_request(request)

# Endpoint: /users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['active','inactive','pending'] , default_enum="active" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("role_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users"
)
req_collection.add_request(request)

# Endpoint: /users, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['create','autoCreate','custCreate','ssoCreate']  ,quoted=True),
    primitives.restler_static_string(""",
    "user_info":
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3','99']  ,quoted=False),
    primitives.restler_static_string("""
        }
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_userspost,
            'dependencies':
            [
                _users_post_email.writer(),
                _users_post_first_name.writer(),
                _users_post_id.writer(),
                _users_post_last_name.writer(),
                _users_post_type.writer()
            ]
        }

    },

],
requestId="/users"
)
req_collection.add_request(request)

# Endpoint: /users/email, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("email="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/email"
)
req_collection.add_request(request)

# Endpoint: /users/me/zak, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("me"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("zak"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/me/zak"
)
req_collection.add_request(request)

# Endpoint: /users/vanity_name, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vanity_name"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("vanity_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/vanity_name"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("action="),
    primitives.restler_fuzzable_group("action", ['disassociate','delete'] , default_enum="disassociate" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transfer_email="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transfer_meeting="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transfer_webinar="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("transfer_recording="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("login_type="),
    primitives.restler_fuzzable_group("login_type", ['0','1','99','100','101']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("login_type="),
    primitives.restler_fuzzable_group("login_type", ['0','1','99','100','101']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "cms_user_id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "company":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "custom_attributes":
        {
            "key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "dept":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_static_string(_users_post_first_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "group_id":"""),
    primitives.restler_static_string(_users_post_id.reader(), quoted=True),
    primitives.restler_static_string(""",
    "host_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "job_title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_static_string(_users_post_last_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "manager":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone_country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone_number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone_numbers":
        {
            "code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "pmi":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_static_string(_users_post_type.reader(), quoted=False),
    primitives.restler_static_string(""",
    "use_pmi":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "vanity_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/assistants, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assistants"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/assistants"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/assistants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assistants"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/assistants"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/assistants, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assistants"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assistants":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/assistants"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/assistants/{assistantId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assistants"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/assistants/{assistantId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/email, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/email"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/meeting_templates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meeting_templates"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/meeting_templates"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/meetings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['scheduled','live','upcoming'] , default_enum="live" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/meetings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/meetings, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("meetings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "agenda":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "recurrence":
        {
            "end_date_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "end_times":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_day":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_week":"""),
    primitives.restler_fuzzable_group("monthly_week", ['-1','1','2','3','4']  ,quoted=False),
    primitives.restler_static_string(""",
            "monthly_week_day":"""),
    primitives.restler_fuzzable_group("monthly_week_day", ['1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string(""",
            "repeat_interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3']  ,quoted=False),
    primitives.restler_static_string(""",
            "weekly_days":"""),
    primitives.restler_fuzzable_group("weekly_days", ['1','2','3','4','5','6','7'] , default_enum="1" ,quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "schedule_for":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "settings":
        {
            "additional_data_center_regions":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "allow_multiple_devices":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "alternative_hosts":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "alternative_hosts_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "approval_type":"""),
    primitives.restler_fuzzable_group("approval_type", ['0','1','2'] , default_enum="2" ,quoted=False),
    primitives.restler_static_string(""",
            "approved_or_denied_countries_or_regions":
                {
                    "approved_list":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "denied_list":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                    ],
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "method":"""),
    primitives.restler_fuzzable_group("method", ['approve','deny']  ,quoted=True),
    primitives.restler_static_string("""
                }
            ,
            "audio":"""),
    primitives.restler_fuzzable_group("audio", ['both','telephony','voip'] , default_enum="both" ,quoted=True),
    primitives.restler_static_string(""",
            "authentication_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_option":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "auto_recording":"""),
    primitives.restler_fuzzable_group("auto_recording", ['local','cloud','none'] , default_enum="none" ,quoted=True),
    primitives.restler_static_string(""",
            "breakout_room":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "rooms":
                    [
                        {
                            "name":"""),
    primitives.restler_static_string(_rooms_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
                            "participants":
                            [
                                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                            ]
                        }
                    ]
                }
            ,
            "close_registration":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "cn_meeting":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "contact_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "contact_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "encryption_type":"""),
    primitives.restler_fuzzable_group("encryption_type", ['enhanced_encryption','e2ee']  ,quoted=True),
    primitives.restler_static_string(""",
            "global_dial_in_countries":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "host_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "in_meeting":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "jbh_time":"""),
    primitives.restler_fuzzable_group("jbh_time", ['0','5','10']  ,quoted=False),
    primitives.restler_static_string(""",
            "join_before_host":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "language_interpretation":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "interpreters":
                    [
                        {
                            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
                            "languages":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
                        }
                    ]
                }
            ,
            "meeting_authentication":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "mute_upon_entry":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "participant_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registration_type":"""),
    primitives.restler_fuzzable_group("registration_type", ['1','2','3'] , default_enum="1" ,quoted=False),
    primitives.restler_static_string(""",
            "show_share_button":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "use_pmi":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "waiting_room":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "watermark":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "start_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "template_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "tracking_fields":
    [
        {
            "field":"""),
    primitives.restler_static_string(_tracking_fields_post_field.reader(), quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3','8'] , default_enum="2" ,quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usersuserIdmeetingspost,
            'dependencies':
            [
                _users__userId__meetings_post_agenda.writer(),
                _users__userId__meetings_post_duration.writer(),
                _users__userId__meetings_post_id.writer(),
                _users__userId__meetings_post_password.writer(),
                _users__userId__meetings_post_start_time.writer(),
                _users__userId__meetings_post_timezone.writer(),
                _users__userId__meetings_post_topic.writer(),
                _users__userId__meetings_post_type.writer()
            ]
        }

    },

],
requestId="/users/{userId}/meetings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/pac, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pac"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/pac"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/password, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("password"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/password"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/permissions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/permissions"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/picture, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("picture"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/picture"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/presence_status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("presence_status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_group("status", ['Do_No_Disturb','Away','Available']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/presence_status"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/recordings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("recordings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mc="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("trash="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_date("2019-06-26", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("trash_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/recordings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/schedulers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("schedulers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/schedulers"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/schedulers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("schedulers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/schedulers"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/schedulers/{schedulerId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("schedulers"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/schedulers/{schedulerId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("login_type="),
    primitives.restler_fuzzable_group("login_type", ['0','1','99','100','101']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("custom_query_fields="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/settings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("option="),
    primitives.restler_fuzzable_group("option", ['meeting_authentication','recording_authentication','meeting_secuirty']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/settings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/settings/virtual_backgrounds, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/settings/virtual_backgrounds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("virtual_backgrounds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/settings/virtual_backgrounds"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['activate','deactivate']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/status"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/token, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/token"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/token, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("token"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['token','zak']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ttl="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/token"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/tsp"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "conference_code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "dial_in_numbers":
    [
        {
            "code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country_label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['toll','tollfree','media_link']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "leader_pin":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "tsp_bridge":"""),
    primitives.restler_fuzzable_group("tsp_bridge", ['US_TSP_TB','EU_TSP_TB']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usersuserIdtsppost,
            'dependencies':
            [
                _users__userId__tsp_post_conference_code.writer(),
                _users__userId__tsp_post_leader_pin.writer(),
                _users__userId__tsp_post_tsp_bridge.writer()
            ]
        }

    },

],
requestId="/users/{userId}/tsp"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "audio_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/tsp/settings"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp/{tspId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['1','2']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/tsp/{tspId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp/{tspId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['1','2']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/tsp/{tspId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/tsp/{tspId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tsp"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['1','2']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "conference_code":"""),
    primitives.restler_static_string(_users__userId__tsp_post_conference_code.reader(), quoted=True),
    primitives.restler_static_string(""",
    "dial_in_numbers":
    [
        {
            "code":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "country_label":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['toll','tollfree','media_link']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "leader_pin":"""),
    primitives.restler_static_string(_users__userId__tsp_post_leader_pin.reader(), quoted=True),
    primitives.restler_static_string(""",
    "tsp_bridge":"""),
    primitives.restler_static_string(_users__userId__tsp_post_tsp_bridge.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/tsp/{tspId}"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/webinar_templates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinar_templates"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/webinar_templates"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/webinars, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{userId}/webinars"
)
req_collection.add_request(request)

# Endpoint: /users/{userId}/webinars, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "agenda":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "recurrence":
        {
            "end_date_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "end_times":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_day":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_week":"""),
    primitives.restler_fuzzable_group("monthly_week", ['-1','1','2','3','4']  ,quoted=False),
    primitives.restler_static_string(""",
            "monthly_week_day":"""),
    primitives.restler_fuzzable_group("monthly_week_day", ['1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string(""",
            "repeat_interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3']  ,quoted=False),
    primitives.restler_static_string(""",
            "weekly_days":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "settings":
        {
            "allow_multiple_devices":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "alternative_hosts":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "approval_type":"""),
    primitives.restler_fuzzable_group("approval_type", ['0','1','2'] , default_enum="2" ,quoted=False),
    primitives.restler_static_string(""",
            "attendees_and_panelists_reminder_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "audio":"""),
    primitives.restler_fuzzable_group("audio", ['both','telephony','voip'] , default_enum="both" ,quoted=True),
    primitives.restler_static_string(""",
            "authentication_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_option":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "auto_recording":"""),
    primitives.restler_fuzzable_group("auto_recording", ['local','cloud','none'] , default_enum="none" ,quoted=True),
    primitives.restler_static_string(""",
            "close_registration":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "contact_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "contact_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email_language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "enforce_login":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "enforce_login_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "follow_up_absentees_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "follow_up_attendees_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "global_dial_in_countries":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "hd_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "host_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "meeting_authentication":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "on_demand":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "panelists_invitation_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "panelists_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "post_webinar_survey":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "practice_session":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "question_and_answer":
                {
                    "allow_anonymous_questions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "answer_questions":"""),
    primitives.restler_fuzzable_group("answer_questions", ['only','all']  ,quoted=True),
    primitives.restler_static_string(""",
                    "attendees_can_comment":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "attendees_can_upvote":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
            ,
            "registrants_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_restrict_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "registration_type":"""),
    primitives.restler_fuzzable_group("registration_type", ['1','2','3'] , default_enum="1" ,quoted=False),
    primitives.restler_static_string(""",
            "show_share_button":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "survey_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "start_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "tracking_fields":
    [
        {
            "field":"""),
    primitives.restler_static_string(_tracking_fields_post_field.reader(), quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_fuzzable_group("type", ['5','6','9'] , default_enum="5" ,quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usersuserIdwebinarspost,
            'dependencies':
            [
                _users__userId__webinars_post_agenda.writer(),
                _users__userId__webinars_post_duration.writer(),
                _users__userId__webinars_post_password.writer(),
                _users__userId__webinars_post_start_time.writer(),
                _users__userId__webinars_post_timezone.writer(),
                _users__userId__webinars_post_topic.writer(),
                _users__userId__webinars_post_type.writer()
            ]
        }

    },

],
requestId="/users/{userId}/webinars"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cancel_webinar_reminder="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("show_previous_occurrences="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "agenda":"""),
    primitives.restler_static_string(_users__userId__webinars_post_agenda.reader(), quoted=True),
    primitives.restler_static_string(""",
    "duration":"""),
    primitives.restler_static_string(_users__userId__webinars_post_duration.reader(), quoted=False),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_static_string(_users__userId__webinars_post_password.reader(), quoted=True),
    primitives.restler_static_string(""",
    "recurrence":
        {
            "end_date_time":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "end_times":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_day":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "monthly_week":"""),
    primitives.restler_fuzzable_group("monthly_week", ['-1','1','2','3','4']  ,quoted=False),
    primitives.restler_static_string(""",
            "monthly_week_day":"""),
    primitives.restler_fuzzable_group("monthly_week_day", ['1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string(""",
            "repeat_interval":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['1','2','3']  ,quoted=False),
    primitives.restler_static_string(""",
            "weekly_days":"""),
    primitives.restler_fuzzable_group("weekly_days", ['1','2','3','4','5','6','7'] , default_enum="1" ,quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "settings":
        {
            "allow_multiple_devices":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "alternative_hosts":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "approval_type":"""),
    primitives.restler_fuzzable_group("approval_type", ['0','1','2'] , default_enum="2" ,quoted=False),
    primitives.restler_static_string(""",
            "attendees_and_panelists_reminder_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "audio":"""),
    primitives.restler_fuzzable_group("audio", ['both','telephony','voip'] , default_enum="both" ,quoted=True),
    primitives.restler_static_string(""",
            "authentication_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "authentication_option":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "auto_recording":"""),
    primitives.restler_fuzzable_group("auto_recording", ['local','cloud','none'] , default_enum="none" ,quoted=True),
    primitives.restler_static_string(""",
            "close_registration":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "contact_email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "contact_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "email_language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "enforce_login":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "enforce_login_domains":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "follow_up_absentees_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "follow_up_attendees_email_notification":
                {
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "type":"""),
    primitives.restler_fuzzable_group("type", ['0','1','2','3','4','5','6','7']  ,quoted=False),
    primitives.restler_static_string("""
                }
            ,
            "global_dial_in_countries":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "hd_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "host_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "meeting_authentication":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "notify_registrants":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "on_demand":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "panelists_invitation_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "panelists_video":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "post_webinar_survey":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "practice_session":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "question_and_answer":
                {
                    "allow_anonymous_questions":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "answer_questions":"""),
    primitives.restler_fuzzable_group("answer_questions", ['only','all']  ,quoted=True),
    primitives.restler_static_string(""",
                    "attendees_can_comment":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "attendees_can_upvote":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
                    "enable":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
                }
            ,
            "registrants_confirmation_email":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_email_notification":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "registrants_restrict_number":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "registration_type":"""),
    primitives.restler_fuzzable_group("registration_type", ['1','2','3'] , default_enum="1" ,quoted=False),
    primitives.restler_static_string(""",
            "show_share_button":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "survey_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "registrants_confirmation_email":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "start_time":"""),
    primitives.restler_static_string(_users__userId__webinars_post_start_time.reader(), quoted=True),
    primitives.restler_static_string(""",
    "timezone":"""),
    primitives.restler_static_string(_users__userId__webinars_post_timezone.reader(), quoted=True),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_static_string(_users__userId__webinars_post_topic.reader(), quoted=True),
    primitives.restler_static_string(""",
    "tracking_fields":
    [
        {
            "field":"""),
    primitives.restler_static_string(_tracking_fields_post_field.reader(), quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "type":"""),
    primitives.restler_static_string(_users__userId__webinars_post_type.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/batch_registrants, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("batch_registrants"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auto_approve":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "registrants":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/batch_registrants"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/panelists, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("panelists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/panelists"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/panelists, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("panelists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/panelists"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/panelists, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("panelists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "panelists":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_webinarswebinarIdpanelistspost,
            'dependencies':
            [
                _webinars__webinarId__panelists_post_id.writer()
            ]
        }

    },

],
requestId="/webinars/{webinarId}/panelists"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/panelists/{panelistId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("panelists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__panelists_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/panelists/{panelistId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/polls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/polls"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/polls, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_webinarswebinarIdpollspost,
            'dependencies':
            [
                _webinars__webinarId__polls_post_id.writer()
            ]
        }

    },

],
requestId="/webinars/{webinarId}/polls"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/polls/{pollId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/polls/{pollId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/polls/{pollId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__polls_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['single','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/polls/{pollId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['pending','approved','denied'] , default_enum="approved" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tracking_source_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_size="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("next_page_token="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "city":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "comments":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "country":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "custom_questions":
    [
        {
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "value":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "first_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "industry":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "job_title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "last_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "no_of_employees":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "org":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "purchasing_time_frame":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "role_in_purchase_process":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "zip":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_webinarswebinarIdregistrantspost,
            'dependencies':
            [
                _webinars__webinarId__registrants_post_id.writer()
            ]
        }

    },

],
requestId="/webinars/{webinarId}/registrants"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants/questions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants/questions, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("questions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "custom_questions":
    [
        {
            "answers":
            [
                """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
            ],
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "type":"""),
    primitives.restler_fuzzable_group("type", ['short','single_radio','single_dropdown','multiple']  ,quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "questions":
    [
        {
            "field_name":"""),
    primitives.restler_fuzzable_group("field_name", ['last_name','address','city','country','zip','state','phone','industry','org','job_title','purchasing_time_frame','role_in_purchase_process','no_of_employees','comments']  ,quoted=True),
    primitives.restler_static_string(""",
            "required":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants/questions"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['approve','cancel','deny']  ,quoted=True),
    primitives.restler_static_string(""",
    "registrants":
    [
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants/status"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants/{registrantId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__registrants_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants/{registrantId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/registrants/{registrantId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("registrants"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_webinars__webinarId__registrants_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("occurrence_id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/registrants/{registrantId}"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "action":"""),
    primitives.restler_fuzzable_group("action", ['end']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/status"
)
req_collection.add_request(request)

# Endpoint: /webinars/{webinarId}/tracking_sources, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("webinars"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tracking_sources"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.zoom.us\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/webinars/{webinarId}/tracking_sources"
)
req_collection.add_request(request)
