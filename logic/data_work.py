from logic.visitor import Visitor

currently_visiting = {}


def filter_data(d_data):
    # print(d_data)
    v = {}
    v["v_name"] = d_data["v_name"]
    v["v_email"] = d_data["v_email"]
    v["v_phone"] = d_data["v_phone"]
    h = {}
    h["h_name"] = d_data["h_name"]
    h["h_email"] = d_data["h_email"]
    h["h_phone"] = d_data["h_phone"]
    h["address"] = d_data["address"]
    return v, h


def create_visitor_obj(v, h):
    v_obj = Visitor(v, h)
    v_obj.submit_and_store()
    v_obj.check_in()
    currently_visiting[v_obj.timestamp] = v_obj
    return v_obj.timestamp


def destroy_visitor_obj(t):
    if t in currently_visiting:
        v_obj = currently_visiting[t]
        v_obj.check_out()
        del currently_visiting[t]
        return True
    return False
