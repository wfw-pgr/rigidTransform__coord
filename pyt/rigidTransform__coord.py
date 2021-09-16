import numpy

# ========================================================= #
# ===  rigidTransform__coord.py                         === #
# ========================================================= #

def rigidTransform__coord( const=None, cnsFile=None ):

    x_,y_,z_ = 0, 1, 2
    
    # ------------------------------------------------- #
    # --- [1] load constants                        --- #
    # ------------------------------------------------- #
    if ( const is None ):
        if ( cnsFile is None ):
            sys.exit( "[rigidTransform__coord] No const & No cnsFile.... " )
        else:
            import nkUtilities.load__constants as lcn
            cnsFile = "dat/parameter.conf"
            const   = lcn.load__constants( inpFile=cnsFile )
            
    # ------------------------------------------------- #
    # --- [2] grid making                           --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    ret     = esg.equiSpaceGrid( x1MinMaxNum=const["x1MinMaxNum"], x2MinMaxNum=const["x2MinMaxNum"], \
                                 x3MinMaxNum=const["x3MinMaxNum"], returnType = "point" )

    # ------------------------------------------------- #
    # --- [3] translate parallel                    --- #
    # ------------------------------------------------- #
    ret[:,x_] = ret[:,x_] - const["xShift1"]
    ret[:,y_] = ret[:,y_] - const["yShift1"]
    ret[:,z_] = ret[:,z_] - const["zShift1"]
    
    # ------------------------------------------------- #
    # --- [4] rotate coordinate                     --- #
    # ------------------------------------------------- #
    import nkBasicAlgs.rotate__vector as rot
    ret = rot.rotate__vector( points=ret, nvec=const["nvec"], theta=const["theta"] )

    # ------------------------------------------------- #
    # --- [5] translate parallel                    --- #
    # ------------------------------------------------- #
    ret[:,x_] = ret[:,x_] - const["xShift2"]
    ret[:,y_] = ret[:,y_] - const["yShift2"]
    ret[:,z_] = ret[:,z_] - const["zShift2"]
    
    # ------------------------------------------------- #
    # --- [6] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=const["outFile"], Data=ret )


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):

    cnsFile = "dat/parameter.conf"
    
    rigidTransform__coord( cnsFile=cnsFile )
