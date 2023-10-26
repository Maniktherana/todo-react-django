import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";

import { Button } from "@/components/ui/button";
import GithubIcon from "./icons/GithubIcon";
import XIcon from "./icons/XIcon";
import ThemeSwitcher from "./ThemeSwitcher";

const Header = () => {
  return (
    <nav>
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
    </nav>
  );
};

export default Header;
