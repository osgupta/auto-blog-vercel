import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import MarkdownIt from 'markdown-it';
import Link from 'next/link';

export async function getStaticProps() {
    const postsDir = path.join(process.cwd(), 'content', 'posts');
    const files = fs.readdirSync(postsDir).filter((f) => f.endsWith('.md'));
    const md = new MarkdownIt();
    const posts = files.map((filename) => {
        const full = path.join(postsDir, filename);
        const raw = fs.readFileSync(full, 'utf8');
        const { data, content } = matter(raw);
        return {
            frontMatter: data,
            content: md.render(content),
            slug: filename.replace(/\.md$/, '')
        };
    });
    return { props: { posts } };
}

export default function Home({ posts }) {
    return (
        <div>
            <h1>Auto Blog</h1>
            <ul>
                {posts.map((p) => (
                    <li key={p.slug}>
                        <Link href={`/posts/${p.slug}`}>
                            <a>{p.frontMatter.title}</a>
                        </Link>{' '}
                        - {p.frontMatter.date}
                    </li>
                ))}
            </ul>
        </div>
    );
}