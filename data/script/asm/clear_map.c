extern void clear_map_asm(int* map, int total);
extern void update_shape_positions_asm(int* data, int count, int y, int x);
extern void scoring_points_asm(int* map, int total);

__declspec(dllexport)
void clear_map(int* map, int rows, int cols)
{
    clear_map_asm(map, rows * cols);
}

__declspec(dllexport)
void update_shape_positions(int* data, int count, int y, int x)
{
    update_shape_positions_asm(data, count, y, x);
}

__declspec(dllexport)
void scoring_points(int* map, int count)
{
    scoring_points_asm(map, count);
}