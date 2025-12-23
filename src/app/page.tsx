export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-zinc-50 to-zinc-100 font-sans dark:from-zinc-950 dark:to-black">
      <main className="flex flex-col items-center justify-center gap-8 px-8 text-center">
        <div className="space-y-4">
          <h1 className="text-6xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 sm:text-7xl md:text-8xl">
            Hello World
          </h1>
          <p className="text-xl text-zinc-600 dark:text-zinc-400 sm:text-2xl">
            欢迎来到我的 Next.js 应用 🎉
          </p>
        </div>
        
        <div className="flex flex-col gap-4 sm:flex-row">
          <a
            className="flex h-12 items-center justify-center rounded-lg bg-zinc-900 px-8 text-base font-medium text-zinc-50 transition-all hover:bg-zinc-800 hover:scale-105 dark:bg-zinc-50 dark:text-zinc-900 dark:hover:bg-zinc-200"
            href="https://nextjs.org/docs"
            target="_blank"
            rel="noopener noreferrer"
          >
            开始学习
          </a>
          <a
            className="flex h-12 items-center justify-center rounded-lg border-2 border-zinc-900 px-8 text-base font-medium text-zinc-900 transition-all hover:bg-zinc-900 hover:text-zinc-50 hover:scale-105 dark:border-zinc-50 dark:text-zinc-50 dark:hover:bg-zinc-50 dark:hover:text-zinc-900"
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            查看源码
          </a>
        </div>
      </main>
    </div>
  );
}
