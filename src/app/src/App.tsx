import { Button } from "@/components/ui/button";
import Header from "@/components/Header";
import { ThemeProvider } from "@/components/theme-provider";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div>
        <Header />
        <Button>Click me</Button>
      </div>
    </ThemeProvider>
  );
}

export default App;
