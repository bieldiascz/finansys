import styles from "@/app/components/MenuVertical/index.module.css";
import Link from "next/link";
import Image from "next/image";

import logo from "../../../../public/logo_finans.png";

import { RiHome4Line } from "react-icons/ri";
import { BsCreditCard } from "react-icons/bs";
import { HiBars3BottomLeft } from "react-icons/hi2";
import { TbReportSearch } from "react-icons/tb";
import { HiOutlineBanknotes } from "react-icons/hi2";
import { LuTarget } from "react-icons/lu";

export default function MenuVertical() {
  return (
    <nav className={styles.menu}>
      <div className={styles.menu_logo_main}>
        <Link className={styles.menu_logo} href="/">
          <Image src={logo} alt="Logo FinanSys" width={45} height={45}></Image>
          <span>FinanSys</span>
        </Link>
      </div>

      <ul className={styles.menu_links}>
        <Link href="/">
          <RiHome4Line size={33} /> <span>Início</span>
        </Link>
        <Link href="/">
          <TbReportSearch size={33} /> <span>Relatórios</span>
        </Link>
        <Link href="/">
          <HiOutlineBanknotes size={33} /> <span>Lançamentos</span>
        </Link>
        <Link href="/">
          <BsCreditCard size={33} /> <span>Seus Cartões</span>
        </Link>
        <Link href="/">
          <LuTarget size={33} /> <span>Metas</span>
        </Link>
      </ul>
    </nav>
  );
}
