import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import MarkdownIt from 'markdown-it';

export async function getStaticPaths() {
    const dir = path.join(process.cwd(), 'content', 'posts');
    const files = fs.readdirSync(dir).filter((f) => f.endsWith('.md'));
    const paths = files.map((f) => ({
        params: {
            slug: f
                .replace(/\.md$/, '') // remove extension
                .replace(/:/g, '') // remove colons
                .replace(/\s+/g, '-') // spaces -> dashes
                .replace(/[^a-zA-Z0-9\-]/g, '-') // other bad chars -> dash
                .replace(/-+/g, '-') // collapse dashes
                .replace(/^-|-$/g, '') // trim edges
        }
    }));
    return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
    const full = path.join(process.cwd(), 'content', 'posts', `${params.slug}.md`);
    const raw = fs.readFileSync(full, 'utf8');
    const { data, content } = matter(raw);
    const md = new MarkdownIt();
    return { props: { frontMatter: data, content: md.render(content) } };
}

export default function Post({ frontMatter, content }) {
    return (
        <article>
            <h1>{frontMatter.title}</h1>
            <div dangerouslySetInnerHTML={{ __html: content }} />
        </article>
    );
}