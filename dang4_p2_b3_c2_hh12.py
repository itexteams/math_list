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


def bt_dang4_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Hàm phụ trợ để thay thế dấu chấm thập phân thành dấu phẩy
            def fmt_num(num):
                return str(num).replace('.', ',')

            # Khai báo biến (Random kích thước lăng trụ)
            a = random.randint(4, 8)  # Chiều dài OA
            b = random.randint(6, 12) # Chiều rộng OC (tịnh tiến y)
            c = random.randint(4, 6)  # Chiều cao OG
            m_x = random.randint(2, a - 1)
            m_z = random.randint(c + 1, c + 3)
            k = random.randint(2, 5)  # Hệ số tỉ lệ điểm P

            # Tính toán các giá trị chính xác bằng Sympy
            P_z = sp.Rational(c, k)
            Q_x = sp.Rational(m_x + a, 2)
            Q_y = b
            Q_z = sp.Rational(m_z + c, 2)

            hinhve=r'''\scalebox{0.6}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]    (114.99,251.2) -- (386.55,251.2) ;
            	\draw [shift={(390.55,251.2)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw [line width=1]    (114.99,251.2) -- (114.99,28.75) ;
            	\draw [shift={(114.99,24.75)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (114.99,251.2) -- (290.89,134.47) ;
            	\draw [shift={(294.22,132.26)}, rotate = 146.43] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw  [line width=1]  (114.99,151.18) -- (280.46,151.18) -- (280.46,251.2) -- (114.99,251.2) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (193.25,100.44) -- (358.73,100.44) ;
            	\draw [line width=1]    (114.99,151.18) -- (193.25,100.44) ;
            	\draw [line width=1]    (280.46,151.18) -- (358.73,100.44) ;
            	\draw [line width=1]    (280.46,251.2) -- (358.73,200.46) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (193.25,200.46) -- (358.73,200.46) ;
            	\draw [line width=1]    (358.73,100.44) -- (358.73,200.46) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (193.25,100.44) -- (193.25,200.46) ;
            	\draw [line width=1]    (235.74,115.92) -- (314,65.17) ;
            	\draw [line width=1]    (358.73,100.44) -- (314,65.17) ;
            	\draw [line width=1]    (235.74,115.92) -- (280.46,151.18) ;
            	\draw [line width=1]    (193.25,100.44) -- (314,65.17) ;
            	\draw [line width=1]    (235.74,115.92) -- (114.99,151.18) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (336.36,82.81) -- (194.46,177.84) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (194.46,177.84) -- (113.61,214.82) ;
            	\draw (100,250.94) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$O$};
            	\draw (381.24,258) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$x$};
            	\draw (294.24,119.83) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$y$};
            	\draw (98.86,23.03) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$z$};
            	\draw (272.05,253.63) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$A$};
            	\draw (362.42,191.6) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$B$};
            	\draw (195.35,206.22) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$C$};
            	\draw (98.39,207.08) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$P$};
            	\draw (174.93,169) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$K$};
            	\draw (183.53,88) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$F$};
            	\draw (308.24,51) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$N$};
            	\draw (338.34,70) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$Q$};
            	\draw (362.42,89.25) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$E$};
            	\draw (282.78,153.5) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$D$};
            	\draw (242.05,110) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$M$};
            	\draw (99,144) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize]  {$G$};
            \end{tikzpicture} }'''

            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Một kho chứa hàng có dạng hình lăng trụ đứng $OADMG.CBENF$ có $OADG$ là hình chữ nhật, $P$ là điểm nằm trên đoạn thẳng $OG$ sao cho $OP = \frac{1}{%s}OG$ và $Q$ là trung điểm của $NE$. Người ta mô hình hoá bằng cách chọn hệ trục toạ độ có gốc toạ độ là điểm $O$ và các trục toạ độ tương ứng như hình vẽ (đơn vị dài trên mỗi trục là $1\text{ m}$). Biết $A\left(%s;0;0\right)$; $C\left(0;%s;0\right)$; $G\left(0;0;%s\right)$; $M\left(%s;0;%s\right)$ (tham khảo hình vẽ).}{%s}''' 
                             % (k, a, b, c, m_x, m_z, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Toạ độ của $N$ là $\\left(%s;%s;%s\\right)$' % (m_x, b, m_z)
            nb_da_1_s = 'Toạ độ của $N$ là $\\left(%s;0;%s\\right)$' % (m_x, m_z)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\overrightarrow{OC} = \\left(0; %s; 0\\right)$. Vì $OADMG.CBENF$ là hình lăng trụ đứng nên mặt bên $OADG$ song song và bằng mặt bên $CBENF$. Phép tịnh tiến theo $\\overrightarrow{OC}$ biến $M\\left(%s; 0; %s\\right)$ thành $N$. Suy ra $N\\left(%s; %s; %s\\right)$.'''
                        % (b, m_x, m_z, m_x, b, m_z))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Tính khoảng cách từ M đến (AGC)
            A_mp = b * c
            B_mp = a * c
            C_mp = a * b
            D_mp = a * b * c
            g = math.gcd(math.gcd(A_mp, B_mp), math.gcd(C_mp, D_mp))
            A_mp //= g
            B_mp //= g
            C_mp //= g
            D_mp //= g

            tu_val = abs(A_mp * m_x + C_mp * m_z - D_mp)
            mau_sq = A_mp**2 + B_mp**2 + C_mp**2
            d_float = tu_val / math.sqrt(mau_sq)
            d_comp = math.floor(d_float)

            # Các đáp án
            th_da_1_d = '\\True Khoảng cách từ điểm $M$ đến mặt phẳng $\\left(AGC\\right)$ lớn hơn $%s\\text{ m}$' % d_comp
            th_da_1_s = 'Khoảng cách từ điểm $M$ đến mặt phẳng $\\left(AGC\\right)$ nhỏ hơn $%s\\text{ m}$' % d_comp
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Phương trình mặt phẳng $\\left(AGC\\right)$ theo đoạn chắn: $\\frac{x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow %sx + %sy + %sz - %s = 0$. \\\\ Khoảng cách $d\\left(M, \\left(AGC\\right)\\right) = \\frac{\\left| %s \\cdot %s + %s \\cdot 0 + %s \\cdot %s - %s \\right|}{\\sqrt{%s^2 + %s^2 + %s^2}} = \\frac{%s}{\\sqrt{%s}} \\approx %s > %s$.'''
                       % (a, b, c, A_mp, B_mp, C_mp, D_mp, A_mp, m_x, B_mp, C_mp, m_z, D_mp, A_mp, B_mp, C_mp, tu_val, mau_sq, fmt_num(round(d_float, 2)), d_comp))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tính góc nhị diện
            nx = m_z - c
            nz = a - m_x
            n1_len_sq = nx**2 + nz**2
            cos_alpha = nz / math.sqrt(n1_len_sq)
            alpha = math.degrees(math.acos(cos_alpha))
            ang_comp = random.choice([30, 45, 60])
            is_greater = alpha > ang_comp

            if is_greater:
                vd_d_str = f"lớn hơn ${ang_comp}^\\circ$"
                vd_s_str = f"nhỏ hơn ${ang_comp}^\\circ$"
            else:
                vd_d_str = f"nhỏ hơn ${ang_comp}^\\circ$"
                vd_s_str = f"lớn hơn ${ang_comp}^\\circ$"

            # Các đáp án
            vd_da_1_d = '\\True Số đo góc nhị diện $\\left[M, DE, F\\right]$ %s' % vd_d_str
            vd_da_1_s = 'Số đo góc nhị diện $\\left[M, DE, F\\right]$ %s' % vd_s_str
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $D\\left(%s;0;%s\\right)$, $E\\left(%s;%s;%s\\right)$. \\\\ Mặt phẳng $\\left(FDE\\right)$ chính là mặt phẳng $z=%s$, có vectơ pháp tuyến $\\overrightarrow{n_2} = \\left(0; 0; 1\\right)$. \\\\ $\\overrightarrow{DM} = \\left(%s; 0; %s\\right)$, $\\overrightarrow{DE} = \\left(0; %s; 0\\right)$. \\\\ Mặt phẳng $\\left(MDE\\right)$ có vectơ pháp tuyến $\\overrightarrow{n_1} = -\\frac{1}{%s}\\left[\\overrightarrow{DM}, \\overrightarrow{DE}\\right] = \\left(%s; 0; %s\\right)$. \\\\ Gọi $\\alpha$ là số đo góc nhị diện $\\left[M, DE, F\\right]$, ta có \\\\ $\\cos \\alpha = \\frac{\\left|\\overrightarrow{n_1} \\cdot \\overrightarrow{n_2}\\right|}{\\left|\\overrightarrow{n_1}\\right| \\left|\\overrightarrow{n_2}\\right|} = \\frac{%s}{\\sqrt{%s^2 + %s^2}} \\approx %s \\Rightarrow \\alpha \\approx %s^\\circ$.''' 
                       % (a, c, a, b, c, c, m_x - a, m_z - c, b, b, nx, nz, nz, nx, nz, fmt_num(round(cos_alpha, 3)), fmt_num(round(alpha, 1))))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Tính dây cáp ngắn nhất
            H_sum = b + float(Q_x)
            V_diff = abs(float(Q_z) - float(P_z))
            min_dist = math.sqrt(H_sum**2 + V_diff**2)
            min_dist_rounded = round(min_dist)

            # Làm tròn để sinh câu đúng/sai
            D_val = min_dist_rounded
            D_false = D_val - 1 if D_val > 10 else D_val + 1

            # Các đáp án
            vdc_da_1_d = '\\True Để lắp đặt camera quan sát trong nhà kho tại vị trí $Q$, đầu thu dữ liệu đặt tại vị trí $P$, người ta thiết kế đường dây cáp nối từ $P$ đến một điểm $K$ trên cạnh $FC$, sau đó nối thẳng đến camera. Cần đoạn dây cáp dài ít nhất $%s\\text{ m}$ (làm tròn đến hàng đơn vị) để nối được từ $P$ đến $Q$' % D_val
            vdc_da_1_s = 'Để lắp đặt camera quan sát trong nhà kho tại vị trí $Q$, đầu thu dữ liệu đặt tại vị trí $P$, người ta thiết kế đường dây cáp nối từ $P$ đến một điểm $K$ trên cạnh $FC$, sau đó nối thẳng đến camera. Cần đoạn dây cáp dài ít nhất $%s\\text{ m}$ (làm tròn đến hàng đơn vị) để nối được từ $P$ đến $Q$' % D_false
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $P\\left(0; 0; %s\\right)$. Trung điểm $Q$ của $NE$ có toạ độ $Q\\left(%s; %s; %s\\right)$. \\\\ $K \\in FC \\Rightarrow K\\left(0; %s; z_K\\right)$ với $0 \\le z_K \\le %s$. \\\\ Quãng đường dây cáp là $L = PK + KQ = \\sqrt{%s^2 + \\left(z_K - %s\\right)^2} + \\sqrt{%s^2 + \\left(%s - z_K\\right)^2}$. \\\\ Áp dụng bất đẳng thức $\\sqrt{u^2 + v^2} + \\sqrt{x^2 + y^2} \\ge \\sqrt{\\left(u+x\\right)^2 + \\left(v+y\\right)^2}$, ta có: \\\\ $L \\ge \\sqrt{\\left(%s + %s\\right)^2 + \\left(z_K - %s + %s - z_K\\right)^2} = \\sqrt{%s^2 + \\left(%s\\right)^2} \\approx %s$. \\\\ Làm tròn đến hàng đơn vị ta được $%s\\text{ m}$.'''
                       % (latex(P_z), latex(Q_x), Q_y, latex(Q_z), b, c, b, latex(P_z), latex(Q_x), latex(Q_z), b, latex(Q_x), latex(P_z), latex(Q_z), fmt_num(round(H_sum, 1)), latex(sp.simplify(Q_z - P_z)), fmt_num(round(min_dist, 2)), D_val))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

