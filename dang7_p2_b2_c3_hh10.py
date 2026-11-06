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


def bt_dang7_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, t = symbols('x y t')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Khởi tạo các điểm sao cho tính toán ra số hữu tỉ đẹp
            xA, yA = -2, 2
            xB, yB = 7, 5
            xC, yC = 4, -5
            # Đường thẳng Delta: 2x + y - 4 = 0 => y = 4 - 2x
            da, db, dc = 2, 1, -4 

            # Nội dung câu hỏi gốc từ ảnh
            noidungcauhoi = r'''Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$ và đường thẳng $\Delta: %sx + y %s = 0$.''' % (
                latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC), latex(da), latex(dc)
            )

            # --- BƯỚC 2: TÍNH TOÁN VÀ TẠO CÁC PHƯƠNG ÁN ---

            ########################################################################
            # Nhận biết - Câu a: Tìm điểm M thuộc Delta sao cho AM = 3
            ########################################################################
            # M(t, 4-2t)
            dist_sq = (t - xA)**2 + (dc/(-db) - (da/-db)*t - yA)**2
            # Với da=2, db=1, dc=-4 => y = 4-2t
            M_t = (t, 4 - 2*t)
            AM_sq = (M_t[0] - xA)**2 + (M_t[1] - yA)**2
            sol_m = solve(AM_sq - 3**2, t)

            M1 = (sol_m[0], 4 - 2*sol_m[0])
            M2 = (sol_m[1], 4 - 2*sol_m[1])

            nb_da_1_d = r'\True Điểm $M \in \Delta$ sao cho $AM = 3$ thì $M\left(%s; %s\right)$ hoặc $M\left(%s; %s\right)$' % ( latex(M1[0]), latex(M1[1]), latex(M2[0]), latex(M2[1])
            )
            nb_da_1_s = r'Điểm $M \in \Delta$ sao cho $AM = 3$ thì $M\left(%s; %s\right)$ hoặc $M\left(%s; %s\right)$' % ( latex(M1[0]+1), latex(M1[1]), latex(M2[0]), latex(M2[1]+1))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Gọi $M(t; 4-2t) \in \Delta$. Ta có $AM^2 = 9 \Leftrightarrow (t+2)^2 + (4-2t-2)^2 = 9 \Leftrightarrow 5t^2 - 4t - 1 = 0$. \\ Giải ra $t=1$ hoặc $t=-\frac{1}{5}$. \\ Vậy $M(1; 2)$ hoặc $M\left(-\frac{1}{5}; \frac{22}{5}\right)$.'''

            ########################################################################
            # Thông hiểu - Câu b: Tìm N thuộc Delta sao cho BN ngắn nhất
            ########################################################################
            # BN ngắn nhất khi N là hình chiếu của B trên Delta
            # Đường thẳng qua B vuông góc Delta: 1(x-7) - 2(y-5) = 0 => x - 2y + 3 = 0
            n_x, n_y = symbols('n_x n_y')
            eq1 = da*n_x + db*n_y + dc
            eq2 = db*(n_x - xB) - da*(n_y - yB)
            sol_n = solve([eq1, eq2], [n_x, n_y])
            xN, yN = sol_n[n_x], sol_n[n_y]
            val_b = xN - yN

            th_da_1_d = r'\True Điểm $N(x_N; y_N) \in \Delta$ sao cho $BN$ ngắn nhất thỏa mãn $x_N - y_N = %s$' % (latex(val_b))
            th_da_1_s = r'Điểm $N(x_N; y_N) \in \Delta$ sao cho $BN$ ngắn nhất thỏa mãn $x_N - y_N = %s$' % (latex(val_b+2))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''$BN$ ngắn nhất khi $N$ là hình chiếu của $B$ trên $\Delta$. \\ Đường thẳng d qua $B$ vuông góc $\Delta$ có phương trình: $x - 2y + 3 = 0$.\\ Tọa độ $N$ là nghiệm của hệ: $\begin{cases} 2x+y-4=0 \\ x-2y+3=0 \end{cases} \Rightarrow N(1; 2)$. \\ Khi đó $x_N - y_N = 1 - 2 = -1$.'''

            ########################################################################
            # Vận dụng - Câu c: P thuộc Delta cách đều A, B
            ########################################################################
            # PA^2 = PB^2
            P_t = (t, 4 - 2*t)
            PA_sq = (P_t[0] - xA)**2 + (P_t[1] - yA)**2
            PB_sq = (P_t[0] - xB)**2 + (P_t[1] - yB)**2
            sol_p = solve(PA_sq - PB_sq, t)
            xP = sol_p[0]
            yP = 4 - 2*xP

            vd_da_1_d = r'\True Điểm $P \in \Delta$ và cách đều hai điểm $A, B$ có tung độ bằng $%s$' % (latex(yP))
            vd_da_1_s = r'Điểm $P \in \Delta$ và cách đều hai điểm $A, B$ có tung độ bằng $%s$' % (latex(yP-1))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Gọi $P(t; 4-2t) \in \Delta$. $P$ cách đều $A, B \Leftrightarrow PA^2 = PB^2 \Leftrightarrow (t+2)^2 + (2-2t)^2 = (t-7)^2 + (-1-2t)^2 \Leftrightarrow 5t^2 - 4t + 8 = 5t^2 - 10t + 50 \Leftrightarrow 6t = 42 \Leftrightarrow t = 7$. \\ Suy ra $y_P = 4 - 2(7) = -10$.'''

            ########################################################################
            # Vận dụng cao - Câu d: Q thuộc Delta sao cho |QB + QC| ngắn nhất
            ########################################################################
            # |QB + QC| = |2QI| với I là trung điểm BC. Ngắn nhất khi Q là hình chiếu của I trên Delta.
            xI, yI = Rational(xB + xC, 2), Rational(yB + yC, 2)
            # Tìm hình chiếu Q của I trên Delta
            q_x, q_y = symbols('q_x q_y')
            eq_q1 = da*q_x + db*q_y + dc
            eq_q2 = db*(q_x - xI) - da*(q_y - yI)
            sol_q = solve([eq_q1, eq_q2], [q_x, q_y])
            xQ = sol_q[q_x]

            vdc_da_1_d = r'\True Điểm $Q \in \Delta$ sao cho $|\vec{QB} + \vec{QC}|$ ngắn nhất có hoành độ bằng $%s$' % (latex(xQ))
            vdc_da_1_s = r'Điểm $Q \in \Delta$ sao cho $|\vec{QB} + \vec{QC}|$ ngắn nhất có hoành độ bằng $%s$' % (latex(xQ+1))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Gọi $I$ là trung điểm của $BC \Rightarrow I\left(\frac{11}{2}; 0\right)$. \\ Ta có $|\vec{QB} + \vec{QC}| = |2\vec{QI}| = 2QI$. \\ Giá trị này nhỏ nhất khi $Q$ là hình chiếu vuông góc của $I$ trên $\Delta$. \\ Đường thẳng đi qua $I$ và vuông góc $\Delta$ có phương trình $x - 2y - \frac{11}{2} = 0$. \\ Tọa độ $Q$ là nghiệm của hệ:\\ $\begin{cases} 2x+y-4=0 \\ x-2y-\frac{11}{2}=0 \end{cases} \Rightarrow Q\left(\frac{27}{10}; -\frac{7}{5}\right)$.'''

            # --- BƯỚC 3: XỬ LÝ ĐÁP ÁN VÀ XUẤT NỘI DUNG ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content   

