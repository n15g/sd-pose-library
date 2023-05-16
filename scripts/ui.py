import gradio as gr


def on_ui_tabs() -> list[tuple[gr.Blocks, str, str]]:
    with gr.Blocks() as pose_library_tab:
        gr.Textbox(label="Testing")

    return [(pose_library_tab, "Pose Library", "poselib_tab")]
