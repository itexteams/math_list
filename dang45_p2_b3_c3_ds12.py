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


def bt_dang45_p2_b3_c3_ds12(self):
    # Khai báo biến và chọn ngẫu nhiên
    x = symbols('x')
    d_val = random.choice([3, 4, 5]) # Hoành độ điểm D
    unit_mm = random.choice([5, 10]) # Đơn vị mm trên hệ trục
    rho_val = random.choice([3.2, 2.8, 4.5]) # Khối lượng riêng g/cm^3

    # Tính toán các hằng số bằng Sympy
    xC = Rational(1, 3)
    yC = 2*sqrt(2)/3
    # Tính phương trình đường thẳng CD
    m = (0 - yC) / (d_val - xC)
    b_line = -m * d_val
    m_latex = latex(m)
    abs_b_latex = latex(abs(b_line))
    sign = "+" if b_line > 0 else "-"

    # Tính thể tích khối tròn xoay theo toạ độ
    V_arc = pi * integrate(1 - x**2, (x, -1, xC))
    V_cone = pi * integrate((m*x + b_line)**2, (x, xC, d_val))
    V_total_oxy = V_arc + V_cone

    # Tính thể tích và khối lượng thực tế
    k = Rational(unit_mm, 10) # Đổi mm sang cm
    V_real = V_total_oxy * (k**3)
    Mass = V_real * Rational(str(rho_val))

    # Xử lý giá trị làm tròn cho câu hỏi VDC
    V_real_eval = float(V_real.evalf())
    threshold_val = Decimal(str(V_real_eval)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    if float(threshold_val) == round(V_real_eval, 2):
        threshold_val = threshold_val + Decimal('0.1')
    is_greater = V_real_eval > float(threshold_val)

    # Định dạng các số chứa dấu phẩy
    rho_str = str(rho_val).replace('.', ',')
    k_str = str(float(k)).replace('.', ',')
    threshold_str = str(threshold_val).replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = ('''Nhân dịp $8/3$, bạn An tặng bạn Bình một sợi dây chuyền có mặt là khối tròn xoay hình giọt nước làm bằng đá Moissanite. Gắn hệ toạ độ $Oxy$ (đơn vị trên mỗi trục là $%s \\text{ mm}$) ta có các số liệu như hình bên dưới. Gọi $f(x)$ là hàm số có đồ thị gồm đoạn thẳng $CD$ và một phần đường tròn tâm $O$, bán kính bằng $1$ đi qua $3$ điểm $A$, $B$, $C$.
    \\begin{center}
    \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    	\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (137.25,174.85) .. controls (138.98,179.52) and (139.93,184.57) .. (139.93,189.83) .. controls (139.93,213.56) and (120.69,232.8) .. (96.96,232.8) .. controls (73.24,232.8) and (54,213.56) .. (54,189.83) .. controls (54,184.91) and (54.83,180.17) .. (56.36,175.77) -- (96.96,189.83) -- cycle ;
    	\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (96.9,75.5) -- (137.25,174.85) -- (96.96,189.83) -- (56.36,175.77) -- cycle ;
    	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (298.6,195.96) .. controls (293.96,197.74) and (288.92,198.75) .. (283.65,198.8) .. controls (259.93,199.07) and (240.48,180.04) .. (240.22,156.31) .. controls (239.96,132.59) and (258.98,113.14) .. (282.71,112.88) .. controls (287.64,112.83) and (292.38,113.6) .. (296.8,115.08) -- (283.18,155.84) -- cycle ;
    	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (397.51,154.52) -- (298.6,195.96) -- (283.18,155.84) -- (296.8,115.08) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (306.9,119.89) -- (312.21,188.39) -- (292.8,197.27) -- (264.91,143.76) -- (290.59,114.53) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (125.63,174.48) .. controls (126.61,177.86) and (127.14,181.48) .. (127.14,185.23) .. controls (127.14,204.25) and (113.53,219.67) .. (96.75,219.67) .. controls (79.96,219.67) and (66.35,204.25) .. (66.35,185.23) .. controls (66.35,181.72) and (66.81,178.34) .. (67.67,175.15) -- (96.75,185.23) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (96.7,93.57) -- (125.24,173.22) -- (96.75,185.23) -- (68.02,173.95) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (116.72,182.53) .. controls (117.02,184.85) and (117.18,187.25) .. (117.18,189.72) .. controls (117.18,208.06) and (108.32,222.92) .. (97.4,222.92) .. controls (86.47,222.92) and (77.61,208.06) .. (77.61,189.72) .. controls (77.61,187.42) and (77.75,185.17) .. (78.01,183.01) -- (97.4,189.72) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (97.37,101.37) -- (115.94,178.14) -- (97.4,189.72) -- (78.7,178.85) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ] (106.73,185.36) .. controls (106.76,186.5) and (106.78,187.66) .. (106.78,188.83) .. controls (106.78,207.66) and (102.58,222.92) .. (97.4,222.92) .. controls (92.21,222.92) and (88.01,207.66) .. (88.01,188.83) .. controls (88.01,187.74) and (88.02,186.66) .. (88.05,185.59) -- (97.4,188.83) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ] (97.38,98.12) -- (106.19,176.95) -- (97.4,188.83) -- (88.52,177.67) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (96.9,83.3) -- (63.23,193.67) -- (63.23,183.27) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (96.9,88.5) -- (85.98,204.72) -- (86.63,181.97) -- cycle ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (129.53,194.97) -- (130.18,204.07) -- (123.68,213.82) -- cycle ;
    	\\draw [line width=1]    (203.1,154.15) -- (436.35,154.15) ;
    	\\draw [shift={(440.35,154.15)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
    	\\draw [line width=1]    (285.65,226.3) -- (285.65,81.45) ;
    	\\draw [shift={(285.65,77.45)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
    	\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (296.8,115.08) -- (296.27,154.13) ;
    	\\draw (265.33,159) node [anchor=north west][inner sep=0.75pt]    {$O$};
    	\\draw (423.33,141) node [anchor=north west][inner sep=0.75pt]    {$x$};
    	\\draw (269.33,72.33) node [anchor=north west][inner sep=0.75pt]    {$y$};
    	\\draw (220.67,130.33) node [anchor=north west][inner sep=0.75pt]    {$A$};
    	\\draw (267.33,92.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
    	\\draw (293.33,95.33) node [anchor=north west][inner sep=0.75pt]    {$C$};
    	\\draw (392.67,130.67) node [anchor=north west][inner sep=0.75pt]    {$D$};
    	\\draw (216.67,159) node [anchor=north west][inner sep=0.75pt]    {$-1$};
    	\\draw (292.67,156.67) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$\\frac{1}{3}$};
    	\\draw (388.67,159) node [anchor=north west][inner sep=0.75pt]    {$3$};
    \\end{tikzpicture}
    \\end{center}''' % (unit_mm))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Đường cong qua ba điểm $A$, $B$, $C$ có phương trình $y = \\sqrt{1 - x^2}$, với $-1 \\le x \\le \\frac{1}{3}$'
    nb_da_1_s = 'Đường cong qua ba điểm $A$, $B$, $C$ có phương trình $y = \\sqrt{1 - x^2}$, với $0 \\le x \\le \\frac{1}{3}$'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Đường tròn tâm $O$ bán kính $R=1$ có phương trình $x^2+y^2=1 \\Rightarrow y = \\pm\\sqrt{1-x^2}$. \\\\
    Phần đường cong qua ba điểm $A$, $B$, $C$ nằm phía trên trục hoành nên có phương trình $y = \\sqrt{1-x^2}$. \\\\
    Dựa vào đồ thị, hoành độ các điểm chạy từ $x_A = -1$ đến $x_C = \\frac{1}{3}$ nên điều kiện là $-1 \\le x \\le \\frac{1}{3}$.'''
                )

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Đoạn thẳng $CD$ có phương trình là $y = %s x %s %s \\, \\left(\\frac{1}{3} \\le x \\le %s\\right)$' % (m_latex, sign, abs_b_latex, d_val)
    th_da_1_s = 'Đoạn thẳng $CD$ có phương trình là $y = %s x %s %s \\, \\left(\\frac{1}{3} \\le x \\le %s\\right)$' % (latex(-m), sign, abs_b_latex, d_val)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Điểm $C$ thuộc đường tròn và có hoành độ $x = \\frac{1}{3}$, tung độ dương nên $y_C = \\sqrt{1 - \\left(\\frac{1}{3}\\right)^2} = \\frac{2\\sqrt{2}}{3}$. Suy ra $C\\left(\\frac{1}{3}; \\frac{2\\sqrt{2}}{3}\\right)$. \\\\
    Điểm $D(%s; 0)$. \\\\
    Đường thẳng $CD$ đi qua hai điểm $C$ và $D$ có hệ số góc $k = \\frac{0 - \\frac{2\\sqrt{2}}{3}}{%s - \\frac{1}{3}} = %s$. \\\\
    Phương trình đường thẳng $CD$: $y - 0 = %s(x - %s) \\Leftrightarrow y = %s x %s %s$. \\\\
    Vì đây là đoạn thẳng giới hạn từ $C$ đến $D$ nên hoành độ thỏa mãn $\\frac{1}{3} \\le x \\le %s$.''' % (d_val, d_val, m_latex, m_latex, d_val, m_latex, sign, abs_b_latex, d_val)
                    )

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Biết khối lượng riêng của đá Moissanite là $\\rho = %s \\, \\text{g/cm}^3$, khi đó khối lượng của mặt dây chuyền là $%s \\, \\text{g}$' % (rho_str, latex(Mass))
    vd_da_1_s = 'Biết khối lượng riêng của đá Moissanite là $\\rho = %s \\, \\text{g/cm}^3$, khi đó khối lượng của mặt dây chuyền là $%s \\, \\text{g}$' % (rho_str, latex(Mass * 2))
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Khối lượng của mặt dây chuyền được tính theo công thức $m = \\rho \\cdot V$. \\\\
    Thể tích $V = %s \\, \\text{cm}^3$. \\\\
    Thay các giá trị đã tính được: $m = %s \\cdot %s = %s \\, (\\text{g})$.''' % (latex(V_real), rho_str, latex(V_real), latex(Mass))
                    )

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    if is_greater:
        vdc_da_1_d = '\\True Thể tích mặt dây chuyền lớn hơn $%s \\, \\text{cm}^3$' % threshold_str
        vdc_da_1_s = 'Thể tích mặt dây chuyền nhỏ hơn $%s \\, \\text{cm}^3$' % threshold_str
    else:
        vdc_da_1_d = '\\True Thể tích mặt dây chuyền nhỏ hơn $%s \\, \\text{cm}^3$' % threshold_str
        vdc_da_1_s = 'Thể tích mặt dây chuyền lớn hơn $%s \\, \\text{cm}^3$' % threshold_str

    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Thể tích khối tròn xoay được tạo thành gồm hai phần: \\\\
    Phần 1: Tạo bởi phần cung tròn $AC$ quay quanh trục $Ox$. Thể tích $V_1 = \\pi \\int_{-1}^{\\frac{1}{3}} \\left(\\sqrt{1-x^2}\\right)^2 \\mathrm{\\,d}x = \\pi \\int_{-1}^{\\frac{1}{3}} (1-x^2) \\mathrm{\\,d}x = \\frac{80\\pi}{81}$. \\\\
    Phần 2: Tạo bởi đoạn thẳng $CD$ quay quanh trục $Ox$ (tạo thành một hình nón). Thể tích $V_2 = \\pi \\int_{\\frac{1}{3}}^{%s} \\left(%s x %s %s\\right)^2 \\mathrm{\\,d}x = %s$. \\\\
    Tổng thể tích trên hệ trục toạ độ là $V_0 = V_1 + V_2 = %s$. \\\\
    Vì mỗi đơn vị trên trục là $%s \\text{ mm} = %s \\text{ cm}$, nên thể tích thực tế của mặt dây chuyền là: \\\\
    $V = V_0 \\cdot (%s)^3 = %s \\cdot %s = %s \\, \\text{cm}^3 \\approx %s \\, \\text{cm}^3$. \\\\
    So sánh giá trị tính được với $%s$, ta kết luận được mệnh đề là đúng.''' % (d_val, m_latex, sign, abs_b_latex, latex(V_cone), latex(V_total_oxy), unit_mm, k_str, k_str, latex(V_total_oxy), latex(k**3), latex(V_real), str(round(V_real_eval, 2)).replace('.', ','), threshold_str)
                    )

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
        str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

