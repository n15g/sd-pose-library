import gradio


def on_ui_tabs():
    with gradio.Blocks() as pose_library_tab:
        gradio.Textbox(label="Testing")

    return pose_library_tab, "Pose Library", "poselib_tab"
