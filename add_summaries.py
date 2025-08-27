import os
import re

# 定义每篇文章的摘要
article_summaries = {
    "2024-05-20-ai-landscape-after-google-io.md": "Google I/O 2024重新定义了AI格局：Gemini 1.5 Pro的200万token上下文窗口、AI搜索的范式转变，以及对整个行业竞争格局的深远影响。深度解析Google如何通过技术创新重塑我们与信息交互的方式。",
    
    "2024-06-04-ai-ui-tension.md": "AI时代的UI设计哲学：当人工智能让界面变得极简，我们是否真的只需要一个对话框？探讨人性化体验与用户掌控感之间的微妙平衡，重新定义智能时代的交互设计。",
    
    "2024-06-09-product-manager-cultivation.md": "算法的尽头是产品的心法：在AI技术日新月异的时代，产品经理如何在技术浪潮中保持初心？从用户需求到商业价值，探索产品思维的本质和修炼之道。",
    
    "2024-06-15-ai-product-manager.md": "AI产品经理到底是风口还是泡沫？从市场需求激增到角色定位模糊，从核心能力要求到未来发展趋势，全面剖析这个备受关注的新兴职位，为求职者和企业提供理性的思考框架。",
    
    "2024-07-17-seven-habits.md": "《高效能人士的七个习惯》深度解读：从个人成长到团队协作，史蒂芬·柯维的经典理论如何指导现代职场人士实现真正的成功？七个习惯的实践指南和现代应用。",
    
    "2024-07-27-sam-altman-y-combinator-speech.md": "Sam Altman的AI未来蓝图：OpenAI CEO在Y Combinator的标志性演讲中，如何描绘人工智能的发展轨迹？从技术突破到社会影响，解析AI领域顶尖思想家的前瞻洞察。",
    
    "2024-07-27-software-3.0-karpathy.md": "软件3.0时代来临：Andrej Karpathy深度解析AI如何重新定义编程范式。从传统编程到神经网络，从代码逻辑到数据驱动，探索软件开发的革命性变革。",
    
    "2024-07-28-elon-musk-thought-blueprint.md": "埃隆·马斯克的思想蓝图：从第一性原理到星际文明，解码这位科技狂人的思维模式。如何用底层逻辑重构复杂问题，实现从0到1的突破性创新？",
    
    "2024-07-28-manus-context-engineering.md": "构建聪明Agent的秘密武器：Manus团队的上下文工程实践全揭秘。为什么不训练模型而要训练上下文？从KV缓存优化到工具管理，深度解析AI代理系统的核心技术。",
    
    "2024-12-15-rag-system-optimization.md": "RAG系统构建完全指南：从文档处理、向量化到检索优化，从生成质量控制到性能评估，深入解析检索增强生成技术的核心要素和实施最佳实践，助你构建高质量的AI知识问答系统。"
}

def add_description_to_markdown(file_path, description):
    """为markdown文件添加description字段"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找front matter的结束位置
    pattern = r'^---\n(.*?)\n---'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        front_matter = match.group(1)
        # 在tags行后添加description
        if 'description:' not in front_matter:
            new_front_matter = front_matter + f'\ndescription: "{description}"'
            new_content = content.replace(match.group(0), f'---\n{new_front_matter}\n---')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已为 {os.path.basename(file_path)} 添加摘要")
        else:
            print(f"⚠️  {os.path.basename(file_path)} 已有摘要，跳过")
    else:
        print(f"❌ 无法解析 {os.path.basename(file_path)} 的front matter")

def main():
    posts_dir = "d:/project/piratelhx.github.io/_posts"
    
    print("🚀 开始为博客文章添加摘要...\n")
    
    for filename, description in article_summaries.items():
        file_path = os.path.join(posts_dir, filename)
        if os.path.exists(file_path):
            add_description_to_markdown(file_path, description)
        else:
            print(f"❌ 文件不存在: {filename}")
    
    print("\n🎉 摘要添加完成！现在每篇文章都有了吸引人的摘要。")

if __name__ == "__main__":
    main()