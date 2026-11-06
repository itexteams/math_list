import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang6_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số tọa độ sao cho hình chiếu bóng (shadow) là số nguyên đẹp
            while True:
                z0 = random.randint(1, 3)     # Mặt phẳng đáy z = z0
                xH = random.randint(3, 6)     # Tâm hình vuông đáy x
                yH = random.randint(3, 6)     # Tâm hình vuông đáy y
                a = random.randint(1, 2)      # Nửa cạnh hình vuông (cạnh = 2a)
                h = random.randint(2, 4)      # Chiều cao chóp
                yL = random.randint(yH + a + 3, 14) # Tung độ đèn (yL > yB)

                yB = yH + a
                yC = yH + a

                # Kiểm tra điều kiện để tB, tS nguyên khi chiếu
                if yL % (yL - yB) != 0: 
                    continue
                if (yL * h) % (yL - yH) != 0: 
                    continue

                tB = yL // (yL - yB)
                tS_h = (yL * h) // (yL - yH)

                xBp = xH + tB * a
                xCp = xH - tB * a
                zBp = z0
                zCp = z0

                xSp = xH
                zSp = z0 + tS_h

                area = tB * a * tS_h
                if area > 0:
                    break

            # Tính tọa độ các điểm
            xA, yA, zA = xH + a, yH - a, z0
            xB, yB, zB = xH + a, yH + a, z0
            xC, yC, zC = xH - a, yH + a, z0
            xD, yD, zD = xH - a, yH - a, z0
            xS, yS, zS = xH, yH, z0 + h
            xL, zL = xH, z0

            # Tính toán cho mệnh đề c (FIXED BUG TẠI ĐÂY)
            # Dùng trực tiếp phép chia thay vì sp.Rational để tránh lỗi với số vô tỉ
            cos_phi = h / sp.sqrt(h**2 + a**2)
            cos_phi_false = a / sp.sqrt(h**2 + a**2)

            # Nội dung hình vẽ TikZ 3D
            tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.6, x={(-0.6cm,-0.4cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}, thick]
            \\draw[->] (0,0,0) -- (10,0,0) node[below left] {$x$};
            \\draw[->] (0,0,0) -- (0,15,0) node[above right] {$y$};
            \\draw[->] (0,0,0) -- (0,0,10) node[above] {$z$};
            \\node[below] at (0,0,0) {$O$};
            \\coordinate (A) at (%s, %s, %s);
            \\coordinate (B) at (%s, %s, %s);
            \\coordinate (C) at (%s, %s, %s);
            \\coordinate (D) at (%s, %s, %s);
            \\coordinate (S) at (%s, %s, %s);
            \\coordinate (L) at (%s, %s, %s);
            \\coordinate (Sp) at (%s, 0, %s);
            \\coordinate (Bp) at (%s, 0, %s);
            \\coordinate (Cp) at (%s, 0, %s);
            \\fill[green!10] (Sp) -- (Bp) -- (Cp) -- cycle;
            \\draw[blue] (Sp) -- (Bp) -- (Cp) -- cycle;
            \\node[above] at (Sp) {$S'$};
            \\node[left] at (Bp) {$B'$};
            \\node[right] at (Cp) {$C'$};
            \\draw[dashed] (A) -- (D) -- (C);
            \\draw (A) -- (B) -- (C);
            \\draw[dashed] (S) -- (D);
            \\draw (S) -- (A) (S) -- (B) (S) -- (C);
            \\node[below left] at (A) {$A$};
            \\node[below] at (B) {$B$};
            \\node[below right] at (C) {$C$};
            \\node[above] at (D) {$D$};
            \\node[above] at (S) {$S$};
            \\filldraw[fill=yellow] (L) circle (3pt) node[right] {$L$};
            \\draw[dashed, thin] (L) -- (B) (B) -- (Bp);
            \\draw[dashed, thin] (L) -- (C) (C) -- (Cp);
            \\draw[dashed, thin] (L) -- (S) (S) -- (Sp);
            \\end{tikzpicture}
            \\end{center}''' % (
                xA, yA, zA, xB, yB, zB, xC, yC, zC, xD, yD, zD, xS, yS, zS, xL, yL, zL, xSp, zSp, xBp, zBp, xCp, zCp
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong một cảnh dựng phim có một ngôi nhà, mái nhà là hình chóp tứ giác đều $S.ABCD$ có chiều cao là $%s$ mét. Trong hệ tọa độ $Oxyz$ (đơn vị đo trên các trục tính bằng mét) với các điểm ở đáy là $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ và $D(%s;%s;%s)$, trong đó $S$ là đỉnh của mái nhà.
            %s''' % (h, xA, yA, zA, xB, yB, zB, xC, yC, zC, xD, yD, zD, tikz_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đáy của mái nhà nằm trên mặt phẳng $z - %s = 0$' % (z0)
            nb_da_1_s = 'Đáy của mái nhà nằm trên mặt phẳng $z - %s = 0$' % (z0 + 1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_nb_1 = ('''Đáy của mái nhà nằm trên mặt phẳng $z = %s \\Leftrightarrow z - %s = 0$''' % (z0, z0))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tọa độ đỉnh của mái nhà là $S(%s;%s;%s)$' % (xS, yS, zS)
            th_da_1_s = 'Tọa độ đỉnh của mái nhà là $S(%s;%s;%s)$' % (xS, yS - 1, zS)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_th_1 = ('''Khối chóp $S.ABCD$ là một tứ giác đều nên $ABCD$ là một hình vuông. \\\\
            Gọi $H$ là hình chiếu của đỉnh $S$ xuống $(ABCD)$ thì $H$ là tâm của hình vuông $ABCD$. \\\\
            Khi đó $H = \\frac{A+C}{2} = (%s;%s;%s)$ nên tọa độ đỉnh $S(%s;%s;%s)$''' % (xH, yH, z0, xS, yS, zS))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Mặt nghiêng của mái nhà $(SBC)$ tạo với mặt phẳng $(Oxz)$ một góc $\\varphi$ thì $\\cos\\varphi = %s$' % (latex(cos_phi))
            vd_da_1_s = 'Mặt nghiêng của mái nhà $(SBC)$ tạo với mặt phẳng $(Oxz)$ một góc $\\varphi$ thì $\\cos\\varphi = %s$' % (latex(cos_phi_false))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Cấu trúc lời giải cơ bản
            n2_y = 2 * a * h
            n2_z = 2 * (a**2)
            base_loigiai_vd_1 = ('''Mặt phẳng $(Oxz)$ có phương trình $y=0$ và có vectơ pháp tuyến $\\vec{n_1} = (0;1;0)$. \\\\
            Ta có $\\vec{SB} = (%s;%s;%s)$ và $\\vec{SC} = (%s;%s;%s)$. \\\\
            Một vectơ pháp tuyến của $(SBC)$ là $\\vec{n_2} = [\\vec{SB}, \\vec{SC}] = (0;%s;%s)$. \\\\
            Khi đó: $\\cos\\varphi = \\frac{|\\vec{n_1} \\cdot \\vec{n_2}|}{|\\vec{n_1}| \\cdot |\\vec{n_2}|} = %s$''' % (
                a, a, -h, -a, a, -h, n2_y, n2_z, latex(cos_phi)
            ))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Một đèn chiếu sáng điểm được đặt tại vị trí $L(%s;%s;%s)$ để chiếu sáng mái nhà từ bên phải. Một màn chắn đặt trùng với mặt phẳng $(Oxz)$, trên đó sẽ xuất hiện bóng của mái nhà và chiếc bóng đó có diện tích bằng $%s$ m$^2$' % (xL, yL, zL, area)
            vdc_da_1_s = 'Một đèn chiếu sáng điểm được đặt tại vị trí $L(%s;%s;%s)$ để chiếu sáng mái nhà từ bên phải. Một màn chắn đặt trùng với mặt phẳng $(Oxz)$, trên đó sẽ xuất hiện bóng của mái nhà và chiếc bóng đó có diện tích bằng $%s$ m$^2$' % (xL, yL, zL, area + random.choice([-2, 2, 4]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_vdc_1 = ('''Ta có: $\\vec{LB} = (%s;%s;%s)$; $\\vec{LC} = (%s;%s;%s)$ và $\\vec{LS} = (%s;%s;%s)$. \\\\
            Do các điểm $S', B', C'$ đều thuộc mặt phẳng $(Oxz)$ nên $y=0$. \\\\
            Phương trình tham số của đường thẳng $LB$:\\\\ $\\begin{cases} x = %s + %st \\\\ y = %s %st \\\\ z = %s \\end{cases} \\Rightarrow %s %st = 0 \\Leftrightarrow t = %s \\Rightarrow B'(%s;0;%s)$. \\\\
            Phương trình tham số của đường thẳng $LC$:\\\\ $\\begin{cases} x = %s %st \\\\ y = %s %st \\\\ z = %s \\end{cases} \\Rightarrow %s %st = 0 \\Leftrightarrow t = %s \\Rightarrow C'(%s;0;%s)$. \\\\
            Phương trình tham số của đường thẳng $LS$:\\\\ $\\begin{cases} x = %s \\\\ y = %s %st \\\\ z = %s + %st \\end{cases} \\Rightarrow %s %st = 0 \\Leftrightarrow t = %s \\Rightarrow S'(%s;0;%s)$. \\\\
            Vậy diện tích của hình chiếu là: $S_{S'B'C'} = \\frac{1}{2} |\\vec{S'C'}, \\vec{S'B'}| = %s$ (m$^2$)''' % (
                a, yB-yL, 0, -a, yC-yL, 0, 0, yH-yL, h,
                xL, a, yL, yB-yL, z0, yL, yB-yL, tB, xBp, zBp,
                xL, -a, yL, yC-yL, z0, yL, yC-yL, tB, xCp, zCp,
                xL, yL, yH-yL, zL, h, yL, yH-yL, tS_h//h, xSp, zSp,
                area
            ))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Sinh lời giải với kết luận đúng/sai linh hoạt tương ứng vào mệnh đề vừa được chọn
            loigiai_nb_1 = base_loigiai_nb_1 + (' nên mệnh đề này đúng.' if '\\True' in nb_da_1 else ' nên mệnh đề này sai.')
            loigiai_th_1 = base_loigiai_th_1 + (' nên mệnh đề này đúng.' if '\\True' in th_da_1 else ' nên mệnh đề này sai.')
            loigiai_vd_1 = base_loigiai_vd_1 + (' nên mệnh đề này đúng.' if '\\True' in vd_da_1 else ' nên mệnh đề này sai.')
            loigiai_vdc_1 = base_loigiai_vdc_1 + (' nên mệnh đề này đúng.' if '\\True' in vdc_da_1 else ' nên mệnh đề này sai.')

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

