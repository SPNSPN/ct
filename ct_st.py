
def every_release (buf_id_read_ms, buf_to_main_ms, rb_release_tool_ms, rb_attach_tool_ms, rb_attach_work_ms, empty_buf_ms):
    rb_nonchange_ms = 0
    rb_nonchange_ms += max(rb_release_tool_ms, empty_buf_ms + buf_id_read_ms)
    rb_nonchange_ms += rb_attach_tool_ms + rb_attach_work_ms

    cv_nonchange_ms = 0
    cv_nonchange_ms += empty_buf_ms + buf_id_read_ms + buf_to_main_ms

    nonchange_ms = max(rb_nonchange_ms, cv_nonchange_ms)


    rb_change_ms = 0
    rb_change_ms += max(rb_release_tool_ms, empty_buf_ms + buf_id_read_ms)
    rb_change_ms += rb_attach_tool_ms + rb_attach_work_ms

    cv_change_ms = 0
    cv_change_ms += empty_buf_ms + buf_id_read_ms + buf_to_main_ms

    change_ms = max(rb_change_ms, cv_change_ms)

    return nonchange_ms, change_ms

def only_change (buf_id_read_ms, buf_to_main_ms, rb_release_tool_ms, rb_attach_tool_ms, rb_attach_work_ms, empty_buf_ms):
    rb_nonchange_ms = 0
    rb_nonchange_ms += empty_buf_ms + buf_id_read_ms
    rb_nonchange_ms += rb_attach_work_ms

    cv_nonchange_ms = 0
    cv_nonchange_ms += empty_buf_ms + buf_id_read_ms + buf_to_main_ms

    nonchange_ms = max(rb_nonchange_ms, cv_nonchange_ms)


    rb_change_ms = 0
    rb_change_ms += empty_buf_ms + buf_id_read_ms
    rb_change_ms += rb_release_tool_ms + rb_attach_tool_ms + rb_attach_work_ms

    cv_change_ms = 0
    cv_change_ms += empty_buf_ms + buf_id_read_ms + buf_to_main_ms

    change_ms = max(rb_change_ms, cv_change_ms)

    return nonchange_ms, change_ms


buf_id_read_ms = 100
buf_to_main_ms = 600
rb_release_tool_ms = 2000
rb_attach_tool_ms = 2000
rb_attach_work_ms = 2000
empty_buf_ms = 1000

change_type_rate = 0.2

print("buf_id_read, buf_to_main, rb_release_tool, rb_attach_tool, rb_attach_work, empty_buf, every_nonchange, every_change, only_nonchange, only_change")
for df_ms in range(0, 10000, 50):

    er_nch_ms, er_ch_ms = every_release(buf_id_read_ms, buf_to_main_ms, rb_release_tool_ms, rb_attach_tool_ms, rb_attach_work_ms, empty_buf_ms + df_ms)
    oc_nch_ms, oc_ch_ms = only_change(buf_id_read_ms, buf_to_main_ms, rb_release_tool_ms, rb_attach_tool_ms, rb_attach_work_ms, empty_buf_ms + df_ms)
    print(", ".join(map(str, [buf_id_read_ms, buf_to_main_ms, rb_release_tool_ms, rb_attach_tool_ms, rb_attach_work_ms, empty_buf_ms + df_ms, er_nch_ms, er_ch_ms, oc_nch_ms, oc_ch_ms])))


