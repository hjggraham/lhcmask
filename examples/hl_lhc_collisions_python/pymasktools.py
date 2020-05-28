import os

def make_links(links_dict, force=False):
    for kk in links_dict.keys():
        if force:
            if os.path.exists(kk):
                os.remove(kk)
        os.symlink(links_dict[kk], kk)

def checks_on_parameter_dict(params):

    assert params['par_nco_IP5']==params['par_nco_IP1']
    assert 'par_beam_norm_emit' in params
    print('Checks on paramter dict passed!')

def check_twiss_value(twiss_df, element_name, keyword, target, tol):
    assert (abs(twiss_df.loc[element_name][keyword] - target) < tol,
                f'Check not passes on {keyword} at {element_name}')

def check_twiss_against_knobs(checks, twiss_df, variable_dicts):
    for cc in checks:
        check_twiss_value(twiss_df,
            element_name=cc['element_name'],
            keyword=cc['keyword'],
            target=variable_dicts['independent_variables'][cc['knob']],
            tol=cc['tol'])


