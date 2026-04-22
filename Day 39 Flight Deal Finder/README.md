## Logic Design



虽然把API成功扒下来了，但成功的喜悦立马被不知道下一步该干什么给浇灭了！于是痛下决心，要把Day 39的整个Flow chart给来个最专业的大包。于是和
Gemini沟通，让他给了我最专业的程序要应该有的思考过程，他还给了我一个彩蛋，即mermaid语法，把一行flowchart内容，GitHub自动渲染成结构图。

```mermaid
graph TD
    A[开始] --> B{是否有本地缓存?}
    B -- 是 --> C[读取 JSON 文件]
    B -- 否 --> D[调用 SerpApi]
    D --> E[保存数据到本地]
    C --> F[解析价格数据]
    E --> F
    F --> G[结束]
