begin
    print(file_path)
    print(file_path(0))
    f = addfile(file_path(0),"r")

    var = f->TMP_P0_L1_GLL0

    f2 = addfile(file_path(1),"r")

    var2 = f2->TMP_P0_L1_GLL0

end