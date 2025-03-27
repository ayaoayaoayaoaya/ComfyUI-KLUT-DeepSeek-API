
MANIFEST = {
    "name": "KLUTDeepSeekAPI",
    "version": (0,1,1),
    "author": "KLUTDEEP",
    "project": "",
    "description": "A DEEPSEEK API node for ComfyUI",
}


from openai import OpenAI






class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""
  def __ne__(self, __value: object) -> bool:
    return False
anyt = AnyType("*")



class KLUTDeepSeekAPI:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "password": True
                }),
                "model": (["deepseek-chat", "deepseek-reasoner"], {
                    "default": "deepseek-chat"
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "Hello, how are you?"
                }),
                "clear_context": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1,
                    "step": 1,
                    "display": "number"
                }),
                "temperature": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.1,
                    "max": 1.0,
                    "step": 0.1
                }),
            },
            "optional": {
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": "You are a helpful assistant."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "call_api"
    CATEGORY = "klut"

    def call_api(self, api_key, model, prompt, clear_context, temperature, system_prompt=None):
        # 初始化客户端
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        
        # 构建消息
        messages = []
        
        if clear_context == 1 and system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        try:
            # 调用API
            response = client.chat.completions.create(
                model=model,  # 使用选择的模型
                messages=messages,
                temperature=temperature,
                stream=False
            )
            
            # 返回响应内容
            return (response.choices[0].message.content,)
            
        except Exception as e:
            error_msg = f"API调用失败: {str(e)}"
            return (error_msg,)

# 节点注册
NODE_CLASS_MAPPINGS = {
    "KLUTDeepSeekAPI": KLUTDeepSeekAPI
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KLUTDeepSeekAPI": "KLUTDeepSeekAPI"
}










#def load_video(meta_batch=None, unique_id=None, memory_limit_mb=None, vae=None,
#               generator=resized_cv_frame_gen, format='None',  **kwargs):
#    format = get_format(format)
#    kwargs['video'] = strip_path(kwargs['video'])
#    downscale_ratio = format.get('dim', (1,))[0]
#    (gen, width, height, fps, duration, total_frames, target_frame_time, yieldable_frames, new_width, new_height, alpha) = meta_batch.inputs[unique_id]
#    memory_limit = None
#    memory_limit = BIGMAX
#    max_loadable_frames = int(memory_limit//(width*height*3*(.1)))
#    original_gen = gen
#    gen = itertools.islice(gen, max_loadable_frames)
#    frames_per_batch = (1920 * 1080 * 16) // (width * height) or 1
#    images = torch.from_numpy(np.fromiter(gen, np.dtype((np.float32, (new_height, new_width, 4 if alpha else 3)))))
#    if len(images) == 0:
#        raise RuntimeError("No frames generated")
#    if 'frames' in format and len(images) % format['frames'][0] != format['frames'][1]:
#        err_msg = f"The number of frames loaded {len(images)}, does not match the requirements of the currently selected format."
#        if len(format['frames']) > 2 and format['frames'][2]:
#            raise RuntimeError(err_msg)
#        div, mod = format['frames'][:2]
#        frames = (len(images) - mod) // div * div + mod
#        images = images[:frames]
#        #Commenting out log message since it's displayed in UI. consider further
#        #logger.warn(err_msg + f" Output has been truncated to {len(images)} frames.")
#    start_time = kwargs['skip_first_frames'] * target_frame_time
#    target_frame_time *= kwargs.get('select_every_nth', 1)
#    return (images,)