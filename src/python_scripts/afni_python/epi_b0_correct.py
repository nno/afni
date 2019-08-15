#!/usr/bin/env python

#ver='1.0' ; date='July 18, 2019'
# + [PT] translating Vinai's original afniB0() function from here:
#   https://github.com/nih-fmrif/bids-b0-tools/blob/master/distortionFix.py
#
#ver='1.1' ; date='July 22, 2019'
# + [PT] updated I/O, help, defaults, dictionaries
#
#
#ver='1.2' ; date='July 22, 2019'
# + [PT] redone shell exec
# + [PT] use diff opts/params for distortion direction and scale
#
#ver='1.3' ; date='July 24, 2019'
# + [PT] add in 3dinfo info to use
# + [PT] expand 3dROIstats options
# + [PT] write out *_cmds.tcsh file, recapitulate utilized param info at top
#
#ver='1.4' ; date='July 25, 2019'
# + [PT] change where scaling is applied-- now separate from 'polarity' issue
# + [PT] updated help (included examples); put beta warning messages!
#
#ver='1.41' ; date='July 26, 2019'
# + [PT] update help; include JSON description
#
#ver='1.5' ; date='July 31, 2019'
# + [PT] rename several variables and opts, to undo my misunderstanding...
# + [PT] EPI back to being required
#
#ver='1.6' ; date='Aug 2, 2019'
# + [PT] added in obliquity checks: should be able to deal with relative 
#        obl diffs between EPI and freq dset (if they exist)
# + [PT] final WARP dset will now be in EPI grid
# + [PT] *still need to check on scaling&recentering of Siemens data*
#
#ver='1.6' ; date='Aug 8, 2019'
# + [PT] update/correct help about Siemens scaling, post-discussion-with-Vinai
#
#ver='1.7' ; date='Aug 12, 2019'
# + [PT] *really* correct help @ Siemens scaling
# + [PT] change internal scaling: *really* demand units of ang freq (rad/s)
# + [PT] py23 compatability of help file-- single dictionary usage!
#
ver='2.0' ; date='Aug 15, 2019'
# + [PT] new parameter scaling of freq dset from Vinai-- better params
# + [PT] apply obliquity info to output
# + [PT] fixed ocmds_fname, if opref contains path
# + [PT] output a useful params file
# + [PT] another py23 compatability fix
#
##########################################################################

import sys, os

import afni_base   as ab
import lib_b0_corr as lb0

# =============================================================================

if __name__ == "__main__" : 

    iopts = lb0.parse_args_b0_corr(sys.argv)

    print("\n++ ================== Start B0 correction ================== \n"
          "   Ver  : {DEF_ver}\n"
          "   Date : {DEF_date}\n"
          "".format( **lb0.ddefs ))

    # Make a mask from a magn dset, if need be
    did_copy_inps = iopts.copy_inps_to_wdir()

    # Make a mask from a magn dset, if need be
    if not(iopts.dset_mask) :
        did_mask_B0 = iopts.mask_B0()

    # Do the main work
    did_B0_corr = iopts.B0_corr()

    iopts.write_params()
    iopts.write_history()

    self_vars = vars( iopts ) 
    print("\n------------")
    print("++ epi_b0_correct.py finishes.")
    print("++ Text of commands :  {ocmds_fname}"
          "".format( **self_vars ))
    print("++ Text of params   :  {opars_fname}"
          "".format( **self_vars ))
    print("++ WARP dset output :  {outdir}/{odset_warp}{dext}"
          "".format( **self_vars ))
    print("++ EPI dset output  :  {outdir}/{odset_epi}{dext}\n"
          "".format( **self_vars ))

    sys.exit(0)



