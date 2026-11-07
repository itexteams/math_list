import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang13_p3_b3_c1_hh12(self):
    # Vòng lặp sinh số đảm bảo luôn có nghiệm thỏa mãn hình học
    while True:
        AB = random.randint(20, 50)
        h = random.randint(2 * AB + 1, 3 * AB - 1)
        ball_bottom = random.randint(int(AB / 3) + 1, AB - 1)

        # Phương trình bậc 2 theo r: (AB + r)^2 = (BM)^2 + 2r^2 với BM = (h - ball_bottom) - r
        # Đặt K = h - ball_bottom:
        # (AB + r)^2 = (K - r)^2 + 2r^2
        # <=> AB^2 + 2*AB*r + r^2 = K^2 - 2*K*r + 3r^2
        # <=> 2*r^2 - 2*(K + AB)*r + (K^2 - AB^2) = 0
        K = h - ball_bottom
        A_coef = 2
        B_coef = -2 * (K + AB)
        C_coef = K**2 - AB**2

        delta = B_coef**2 - 4 * A_coef * C_coef
        if delta > 0:
            # Tìm các nghiệm thực
            r1 = (-B_coef - math.sqrt(delta)) / (2 * A_coef)
            r2 = (-B_coef + math.sqrt(delta)) / (2 * A_coef)

            # Bán kính quả bóng phải dương và tâm I phải nằm dưới điểm treo B (r < K)
            valid_r = [val for val in (r1, r2) if 0 < val < K]
            if valid_r:
                r_val = valid_r[0]
                break

    # Đường kính d = 2*r
    d_val = 2 * r_val

    # Làm tròn theo chuẩn Decimal
    r_round = Decimal(str(r_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    dk_round = Decimal(str(d_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    r_str = str(r_round).replace('.', ',')
    dk_str = str(dk_round).replace('.', ',')
    K_str = str(K)

    # Phương trình bậc 2 hiển thị trong lời giải
    r_sym = symbols('r')
    pt_bac2 = 2 * r_sym**2 - 2 * (K + AB) * r_sym + (K**2 - AB**2)

    # Nội dung câu hỏi
    noidungcauhoi = r"""\immini{Trong không gian $Oxyz$, một quả bóng hình cầu được treo trong góc giữa hai bức tường vuông góc và mặt đất.
Điểm $B$ nằm trên giao tuyến của hai bức tường, cách mặt đất %s cm.
Sợi dây treo bóng có độ dài $AB = %s$ cm, nối từ $B$ đến mặt ngoài quả bóng.
Quả bóng tiếp xúc với cả hai tường và cách mặt đất %s cm (minh hoạ như hình bên).
Hỏi đường kính quả bóng là bao nhiêu cm (kết quả làm tròn đến hàng phần chục)?
}
{\definecolor{ffdxqq}{rgb}{1.,0.8431372549019608,0.}
\scalebox{0.5}{ 
\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
\clip(-6.983965496860758,-3.314679394875518) rectangle (4.6216781291272175,7.40096088556118);
\fill[line width=1.pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.1] (-6.,6.) -- (-6.,0.) -- (-4.,-1.) -- (0.,0.) -- (2.,-2.) -- (4.002958630446015,-1.009143782064421) -- (4.023283705182322,5.129028788300249) -- (2.,4.) -- (0.,6.) -- (-4.,5.) -- cycle;
\fill[line width=1.pt,fill=black,pattern=north east lines,pattern color=black] (-1.5,-1.) -- (-0.5,-1.) -- (-0.49644128445539454,-1.2049086154202542) -- (-1.5005432683471505,-1.2105181237101523) -- cycle;
\draw [line width=1.pt] (0.,0.)-- (0.,5.);
\draw [line width=1.pt] (-1.,2.) circle (1.4142135623730951cm);
\draw [line width=1.pt] (0.,5.)-- (-0.7336351632734832,3.388902362931123);
\draw [line width=1.pt] (-1.,0.5857864376269049)-- (-1.,-1.);
\draw [->,line width=1.pt,dash pattern=on 4pt off 4pt] (0.,0.) -- (0.,7.);
\draw [->,line width=1.pt,dash pattern=on 4pt off 4pt] (0.,0.) -- (-6.048624092638949,-1.5167098736908888);
\draw [->,line width=1.pt,dash pattern=on 4pt off 4pt] (0.,0.) -- (3.,-3.);
\draw [line width=1.pt] (0.,6.)-- (-4.,5.);
\draw [line width=1.pt] (-4.,5.)-- (-6.,6.);
\draw [line width=1.pt] (-6.,0.)-- (-4.,-1.);
\draw [line width=1.pt] (-6.,6.)-- (-6.,0.);
\draw [line width=1.pt] (0.,6.)-- (2.,4.);
\draw [line width=1.pt] (2.,4.)-- (4.023283705182322,5.129028788300249);
\draw [line width=1.pt] (2.,-2.)-- (4.002958630446015,-1.009143782064421);
\draw [line width=1.pt] (4.002958630446015,-1.009143782064421)-- (4.023283705182322,5.129028788300249);
\draw [line width=1.pt] (-4.,-1.)-- (0.,0.);
\draw [line width=1.pt] (0.,0.)-- (2.,-2.);
\draw [line width=1.pt] (0.,5.)-- (0.,6.);
\draw [rotate around={-0.9877603996398072:(-0.9954765069272391,2.002432462764389)},line width=1.pt,dash pattern=on 4pt off 4pt] (-0.9954765069272391,2.002432462764389) ellipse (1.4073996068528722cm and 0.6291687547243985cm);
\draw [shift={(-1.9338535384625561,2.0793858059249066)},line width=1.pt]  plot[domain=3.2808185075204133:4.2427695351289385,variable=\t]({1.*0.47331734530381814*cos(\t r)+0.*0.47331734530381814*sin(\t r)},{0.*0.47331734530381814*cos(\t r)+1.*0.47331734530381814*sin(\t r)});
\draw [shift={(-0.9549077349708847,3.9700456343895083)},line width=1.pt]  plot[domain=4.236101212592304:5.1239462462137,variable=\t]({1.*2.6023722299408205*cos(\t r)+0.*2.6023722299408205*sin(\t r)},{0.*2.6023722299408205*cos(\t r)+1.*2.6023722299408205*sin(\t r)});
\draw [shift={(-0.1005759942529458,2.068184582087821)},line width=1.pt]  plot[domain=5.081118415670269:6.133324250011472,variable=\t]({1.*0.5180292067236515*cos(\t r)+0.*0.5180292067236515*sin(\t r)},{0.*0.5180292067236515*cos(\t r)+1.*0.5180292067236515*sin(\t r)});
\draw [->,line width=1.pt] (-1.3886234932666535,1.7334697093098352) -- (-1.,2.);
\draw [->,line width=1.pt] (-1.3886234932666535,1.7334697093098352) -- (-1.7430310821555102,1.4898837822537128);
\draw (-0.4,0) node[anchor=north west] {$O$};
\draw (-6.04056195057646,-0.876070228065173) node[anchor=north west] {$x$};
\draw (2.8950716387578406,-2.3) node[anchor=north west] {$y$};
\draw (-0.4869410743368146,7.205160149539911) node[anchor=north west] {$z$};
\draw (-1.1811436838667702,4.090148440110639) node[anchor=north west] {$A$};
\draw (-0.5047411412478391,5.478553659170544) node[anchor=north west] {$B$};
\draw (-1.6795455573754563,2.3101417490081975) node[anchor=north west] {$r$};
\end{tikzpicture} } }""" % (h, AB, ball_bottom)

    # Lời giải chi tiết - dùng {{...}} để thoát cặp ngoặc nhọn của LaTeX
    loigiai = rf"""Gọi $I$ là tâm quả bóng, bán kính $r$ ($0 < r < {K}$).\\
Gọi $M$ là hình chiếu của tâm $I$ lên trục $Oz$, ta có $M(0;0;z_I)$ với $z_I = {ball_bottom} + r$.\\
Tọa độ điểm $B(0;0;{h})$, suy ra $BM = {h} - ({ball_bottom} + r) = {K_str} - r$.\\
Vì quả bóng tiếp xúc với hai mặt tường $(xOz)$ và $(yOz)$ nên khoảng cách từ $I$ đến hai mặt phẳng này đều bằng $r$, do đó $d(I, Oz) = MI = \sqrt{{r^2 + r^2}} = r\sqrt{{2}}$.\\
Độ dài đoạn nối từ $B$ đến tâm $I$ là:
$BI = AB + r = {AB} + r$.\\
Xét tam giác $BMI$ vuông tại $M$, ta có hệ thức:
$BI^2 = BM^2 + MI^2$\\
$\Leftrightarrow ({AB} + r)^2 = ({K_str} - r)^2 + 2r^2$\\
$\Leftrightarrow {latex(pt_bac2)} = 0 \Rightarrow r \approx {r_str}\text{{ cm}}$ (do $0 < r < {K}$).\\
Vậy đường kính quả bóng là $2r \approx {dk_str}\text{{ cm}}$."""

    # Đáp án ngắn
    dapan = rf"\shortans[0]{{{dk_str}}}"

    # Xuất nội dung hoàn chỉnh
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n'
        + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n' )
    return content
