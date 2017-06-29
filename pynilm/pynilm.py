from simsetup import Setup

def nilm_eval(setup_path):
    startup()
    try:
        setup = Setup.from_yaml(setup_path)
    except Exception:
        raise ValueError("Error parsing configuration file")
    print("Loaded setup: {}".format(setup))
