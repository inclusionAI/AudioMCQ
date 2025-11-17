#!/usr/bin/env python3
"""
Simple Audio Choice GRPO Plugin - Basic accuracy reward function
"""

import re
from swift.plugin import ORM, orms


def print_comparison_compact(completions, solution):
    print("\n📊 Completion vs Solution Comparison:")
    print("-" * 60)
    
    max_len = max(len(completions), len(solution))
    
    for i in range(max_len):
        comp = completions[i] if i < len(completions) else "N/A"
        sol = solution[i] if i < len(solution) else "N/A"
        
        print(f"{i:2d}. '{comp}' vs '{sol}'")
    
    print("-" * 60)


def audio_choice_accuracy_reward(completions, solution, **kwargs):
    """
    Simple reward function that checks if the completion matches the solution exactly.
    """

    print_comparison_compact(completions, solution)
    
    rewards = []
    
    for content, sol in zip(completions, solution):
        reward = 0.0
        
        try:
            # Extract answer from solution (ground truth)
            sol_match = re.search(r"<answer>(.*?)</answer>", sol, re.DOTALL | re.IGNORECASE)
            ground_truth = sol_match.group(1).strip() if sol_match else sol.strip()
            
            # Extract answer from model output
            content_match = re.search(r"<answer>(.*?)</answer>", content, re.DOTALL | re.IGNORECASE)
            student_answer = content_match.group(1).strip() if content_match else content.strip()
            
            # Exact string matching (case-insensitive)
            if student_answer.lower() == ground_truth.lower():
                reward = 1.0
                
        except Exception as e:
            reward = 0.0
            print(f"Error in reward calculation: {e}")
        
        rewards.append(reward)
    
    return rewards

def external_format_reward(completions, solution, **kwargs):
    """
    Format reward function that checks if the completion is completely surrounded by <answer>...</answer> tags.
    Returns 1.0 if the format is correct (entire content wrapped), 0.0 otherwise.
    """
    rewards = []
    
    for content in completions:
        reward = 0.0
        
        try:
            # Strip whitespace from content for accurate checking
            stripped_content = content.strip()
            
            # Check if content starts with <answer> and ends with </answer>
            if (stripped_content.startswith('<answer>') and 
                stripped_content.endswith('</answer>')):
                
                # Additional check: ensure there's only one <answer> at start and one </answer> at end
                # This prevents cases like <answer>text</answer>extra or extra<answer>text</answer>
                answer_start_count = stripped_content.count('<answer>')
                answer_end_count = stripped_content.count('</answer>')
                
                if (answer_start_count == 1 and answer_end_count == 1 and
                    stripped_content.find('<answer>') == 0 and
                    stripped_content.rfind('</answer>') == len(stripped_content) - 9):
                    reward = 1.0
                    # print(f"Format correct: Content properly wrapped in <answer> tags")
                else:
                    reward = 0.0
                    # print(f"Format incorrect: Multiple or misplaced <answer> tags")
            else:
                reward = 0.0
                # print(f"Format incorrect: Content not properly wrapped in <answer> tags")
                
        except Exception as e:
            reward = 0.0
            print(f"Error in format reward calculation: {e}")
        
        rewards.append(reward)
    
    return rewards

# ORM class wrapper for SWIFT integration
class AudioChoiceAccuracyORM(ORM):
    def __call__(self, completions, solution, **kwargs):
        return audio_choice_accuracy_reward(completions, solution, **kwargs)

class ExternalFormatORM(ORM):
    def __call__(self, completions, solution, **kwargs):
        return external_format_reward(completions, solution, **kwargs)

# Register reward functions
orms['external_audio_choice_accuracy'] = AudioChoiceAccuracyORM
orms['external_format'] = ExternalFormatORM

print("Audio choice accuracy reward function registered successfully!")
print("External format reward function registered successfully!")