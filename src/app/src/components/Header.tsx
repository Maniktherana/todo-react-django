import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";

import { Button } from "@/components/ui/button";
import GithubIcon from "./icons/GithubIcon";
import XIcon from "./icons/XIcon";
import ThemeSwitcher from "./ThemeSwitcher";
import ListIcon from "./icons/ListIcon";

const Header = () => {
  return (
    <header className="border-b">
      <div className="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-2">
        <div className="flex items-center space-x-4">
          <div className="flex justify-center items-center space-x-3">
            <ListIcon />
            <h1 className="text-xl select-none">Todoer</h1>
          </div>
        </div>
        <NavigationMenu>
          <NavigationMenuList>
            <NavigationMenuItem>
              <Button
                variant="ghost"
                size="icon"
                className="hover:text-volt"
                onClick={() =>
                  window.open("https://twitter.com/ManikMkr", "_blank")
                }
              >
                <XIcon />
              </Button>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <Button
                variant="ghost"
                size="icon"
                className="hover:text-volt"
                onClick={() =>
                  window.open(
                    "https://github.com/Maniktherana/todo-react-django",
                    "_blank"
                  )
                }
              >
                <GithubIcon />
              </Button>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <ThemeSwitcher />
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
      </div>
    </header>
  );
};

export default Header;
