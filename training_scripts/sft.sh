# 18GiB * 2
nproc_per_node=your_number_of_nodes
export NPROC_PER_NODE=$nproc_per_node

swift sft \
    --model 'path_to_Qwen__Qwen2.5-Omni-7B' \
    --train_type full \
    --dataset 'path_to_dataset' \
    --torch_dtype bfloat16 \
    --num_train_epochs 2 \
    --per_device_train_batch_size 20 \
    --per_device_eval_batch_size 20 \
    --learning_rate 1e-6 \
    --gradient_accumulation_steps 1 \
    --save_only_model True \
    --padding_side left \
    --eval_steps 250 \
    --save_steps 250 \
    --logging_steps 1 \
    --max_length 1024 \
    --output_dir 'path_to_output_dir' \
    --deepspeed zero2 \
    --model_type 'qwen2_5_omni' \
    --warmup_ratio 0.05 \
    --lr_scheduler_type 'cosine' \
    --system 'You are an audio understanding model that answers multiple choice questions based on audio content.' \
    --freeze_llm false \
    --freeze_vit false \
    --freeze_aligner false \