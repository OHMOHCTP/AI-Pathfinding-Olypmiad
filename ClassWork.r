PROCEDURE LogEvents()
    DECLARE FileHandle : INTEGER
    DECLARE i : INTEGER

    FileHandle ← OPENFILE("LoginFile.txt", "APPEND")

    FOR i ← 0 TO 499
        IF LogArray[i] ≠ "Empty" THEN
            WRITEFILE(FileHandle, LogArray[i])
        ENDIF
    NEXT i

    CLOSEFILE(FileHandle)
ENDPROCEDURE