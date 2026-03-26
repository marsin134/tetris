.intel_syntax noprefix
.global clear_map_asm

clear_map_asm:
    mov r8, rcx
    mov rcx, rdx

loop_start_clear:
    test rcx, rcx
    je done_clear

    mov dword ptr [r8], 0
    add r8, 4

    dec rcx
    jmp loop_start_clear

done_clear:
    ret


.global update_shape_positions_asm

update_shape_positions_asm:
    mov r10, rcx
    mov rcx, rdx

loop_blocks_update:
    test rcx, rcx
    je done_update

    # block[0] += y
    mov eax, dword ptr [r10]
    add eax, r8d
    mov dword ptr [r10], eax

    # block[1] += x
    mov eax, dword ptr [r10 + 4]
    add eax, r9d
    mov dword ptr [r10 + 4], eax

    add r10, 8
    dec rcx
    jmp loop_blocks_update

done_update:
    ret

.intel_syntax noprefix

.global scoring_points_asm

scoring_points_asm:
    # rcx - указатель на строку map_block[y]
    # rdx - количество элементов в строке (length of map_block[y])
    xor eax, eax           # eax = 0 (флаг для проверки наличия нуля, 0 если найден ноль, иначе 1)

loop_check:
    cmp dword ptr [rcx], 0  # проверка текущего элемента на 0
    je found_zero            # если найден 0, переходим к found_zero
    add rcx, 4               # переход к следующему элементу строки
    dec rdx
    jnz loop_check           # если не конец строки, продолжаем проверку

    # Если все элементы не нули
    mov eax, 1               # флаг = 1, строка не содержит нулей
    ret

found_zero:
    mov eax, 0               # строка содержит 0, флаг = 0
    ret