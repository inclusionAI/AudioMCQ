echo "Starting GRPO training..."
NPROC_PER_NODE=your_number_of_nodes \
swift rlhf \
    --rlhf_type grpo \
    --train_type full \
    --model path_to_Qwen__Qwen2.5-Omni-7B \
    --model_type qwen2_5_omni \
    --dataset 'path_to_dataset' \
    --output_dir path_to_output_dir \
    --external_plugins plugin.py \
    --reward_funcs external_audio_choice_accuracy external_format \
    --reward_weights 2.0 0.5 \
    --learning_rate 1e-6 \
    --lr_scheduler_type "cosine" \
    --num_generations 8 \
    --num_iterations 1 \
    --beta 0.001 \
    --warmup_ratio 0.01 \
    --temperature 1.5 \
    --top_k 4 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --max_length 2048 \
    --max_completion_length 128 \
    --max_steps 2000 \
    --gradient_accumulation_steps 1 \
    --eval_steps 100 \
    --save_steps 100 \
    --val_dataset 'path_to_val_dataset' \
    --save_total_limit -1 \
    --logging_steps 1 \
    --dataloader_num_workers 16 \
    --deepspeed zero2 \
    --log_completions false \
    --async_generate false \
    --torch_dtype bfloat16 \
    --save_strategy 'steps' \
    --freeze_llm false \
    --freeze_vit false \
    --freeze_aligner false \
    --split_dataset_ratio 0 \
    --system 'You are an audio understanding model that answers multiple choice questions based on audio content.' \

echo "Training completed!"