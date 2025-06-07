docs:
    # 生成文档
    echo "开始生成文档..."
    make html && \
    echo "文档生成成功"

# 预览编译好的 HTML 文档
preview:
     cd build/html && python3 -m http.server 8000