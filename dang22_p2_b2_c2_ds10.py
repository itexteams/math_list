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


def bt_dang22_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên các tham số bài toán
            while True:
                C1 = 9
                C2 = 3
                X0 = 1
                C3 = random.choice([6, 9])

                # Tọa độ các đỉnh của miền nghiệm
                # A là giao điểm d1 (3x+2y=9) và d2 (x-2y=3)
                xA, yA = 3, 0

                # B là giao điểm d2 (x-2y=3) và d3 (x+y=C3)
                yB = int((C3 - 3) / 3)
                xB = C3 - yB

                # C là giao điểm d3 (x+y=C3) và d4 (x=1)
                xC, yC = 1, C3 - 1

                # D là giao điểm d4 (x=1) và d1 (3x+2y=9)
                xD, yD = 1, 3

                # Số nguyên m thỏa mãn (3; m) là nghiệm
                m_max = C3 - 3
                m_count = m_max + 1
                fake_m_count = m_count + random.choice([1, 2])

                break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình: $\\begin{cases} 3x + 2y \\ge %s \\\\ x - 2y \\le %s \\\\ x + y \\le %s \\\\ x \\ge %s \\end{cases} \\quad (I)$.''' % (C1, C2, C3, X0))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Hệ bất phương trình $(I)$ là hệ bất phương trình bậc nhất hai ẩn'
            nb_da_1_s = 'Hệ bất phương trình $(I)$ không phải là hệ bất phương trình bậc nhất hai ẩn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True $(3; 2)$ là một nghiệm của hệ bất phương trình $(I)$'
            th_da_1_s = '$(3; 2)$ không phải là một nghiệm của hệ bất phương trình $(I)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Có %s số nguyên $m$ để $(3; m)$ là một nghiệm của hệ bất phương trình $(I)$' % m_count
            vd_da_1_s = 'Có %s số nguyên $m$ để $(3; m)$ là một nghiệm của hệ bất phương trình $(I)$' % fake_m_count
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Miền nghiệm của hệ bất phương trình là miền tứ giác'
            vdc_da_1_s = 'Miền nghiệm của hệ bất phương trình là miền tam giác'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

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

            # Lời giải Nhận biết
            if '\\True' in nb_da_1:
                loigiai_nb_1 = ('Hệ bất phương trình $(I)$ gồm bốn bất phương trình bậc nhất hai ẩn $x, y$. Do đó đây là hệ bất phương trình bậc nhất hai ẩn. Phát biểu trên là đúng.')
            else:
                loigiai_nb_1 = ('Hệ bất phương trình $(I)$ gồm bốn bất phương trình bậc nhất hai ẩn $x, y$. Do đó đây là hệ bất phương trình bậc nhất hai ẩn. Phát biểu trên là sai.')

            # Lời giải Thông hiểu
            if '\\True' in th_da_1:
                loigiai_th_1 = ('Thay $x = 3, y = 2$ vào từng bất phương trình của hệ $(I)$ ta có: \\\\'
                                '$3 \\cdot 3 + 2 \\cdot 2 = 13 \\ge %s$ (đúng) \\\\'
                                '$3 - 2 \\cdot 2 = -1 \\le %s$ (đúng) \\\\'
                                '$3 + 2 = 5 \\le %s$ (đúng) \\\\'
                                '$3 \\ge %s$ (đúng). \\\\'
                                'Vậy $(3; 2)$ là một nghiệm của hệ bất phương trình $(I)$. Phát biểu trên là đúng.' % (C1, C2, C3, X0))
            else:
                loigiai_th_1 = ('Thay $x = 3, y = 2$ vào từng bất phương trình của hệ $(I)$ ta có: \\\\'
                                '$3 \\cdot 3 + 2 \\cdot 2 = 13 \\ge %s$ (đúng) \\\\'
                                '$3 - 2 \\cdot 2 = -1 \\le %s$ (đúng) \\\\'
                                '$3 + 2 = 5 \\le %s$ (đúng) \\\\'
                                '$3 \\ge %s$ (đúng). \\\\'
                                'Vậy $(3; 2)$ là một nghiệm của hệ bất phương trình $(I)$. Phát biểu trên là sai.' % (C1, C2, C3, X0))

            # Lời giải Vận dụng
            m_list_str = ", ".join(str(i) for i in range(0, m_max + 1))
            if '\\True' in vd_da_1:
                loigiai_vd_1 = ('Thay $x = 3$ và $y = m$ vào hệ bất phương trình $(I)$ ta được: \\\\'
                                '$\\begin{cases} 3 \\cdot 3 + 2m \\ge %s \\\\ 3 - 2m \\le %s \\\\ 3 + m \\le %s \\\\ 3 \\ge %s \\end{cases} \\iff \\begin{cases} 2m \\ge 0 \\\\ -2m \\le 0 \\\\ m \\le %s \\end{cases} \\iff 0 \\le m \\le %s$. \\\\'
                                'Vì $m \\in \\mathbb{Z}$ nên $m \\in \\{%s\\}$. Có %s số nguyên $m$ thỏa mãn. Do đó phát biểu trên là đúng.' % (C1, C2, C3, X0, m_max, m_max, m_list_str, m_count))
            else:
                loigiai_vd_1 = ('Thay $x = 3$ và $y = m$ vào hệ bất phương trình $(I)$ ta được: \\\\'
                                '$\\begin{cases} 3 \\cdot 3 + 2m \\ge %s \\\\ 3 - 2m \\le %s \\\\ 3 + m \\le %s \\\\ 3 \\ge %s \\end{cases} \\iff \\begin{cases} 2m \\ge 0 \\\\ -2m \\le 0 \\\\ m \\le %s \\end{cases} \\iff 0 \\le m \\le %s$. \\\\'
                                'Vì $m \\in \\mathbb{Z}$ nên $m \\in \\{%s\\}$. Có %s số nguyên $m$ thỏa mãn. Do đó phát biểu trên là sai.' % (C1, C2, C3, X0, m_max, m_max, m_list_str, m_count))

            # Tính toán các thông số vẽ hình TikZ
            max_coord = max(xB, yC)
            S = max_coord / 3.5

            xA_p, yA_p = xA / S, yA / S
            xB_p, yB_p = xB / S, yB / S
            xC_p, yC_p = xC / S, yC / S
            xD_p, yD_p = xD / S, yD / S

            # Giao điểm của các đường thẳng d1, d2, d3, d4 với khung clip x=-1 và x=5
            # d1: 3x + 2y = 9 => y = (9 - 3x)/2
            l1_y_m1 = (9/S + 3) / 2.0
            l1_y_5 = (9/S - 15) / 2.0

            # d2: x - 2y = 3 => y = (x - 3)/2
            l2_y_m1 = (-1 - 3/S) / 2.0
            l2_y_5 = (5 - 3/S) / 2.0

            # d3: x + y = C3 => y = C3 - x
            l3_y_m1 = C3/S + 1.0
            l3_y_5 = C3/S - 5.0

            # d4: x = 1
            l4_x = 1.0 / S

            # Lời giải Vận dụng cao
            if '\\True' in vdc_da_1:
                eval_vdc = "Do đó phát biểu trên là đúng."
            else:
                eval_vdc = "Do đó phát biểu trên là sai."

            loigiai_vdc_1 = ('''Vẽ các đường thẳng: \\\\
            $d_1: 3x + 2y = %s$, $d_2: x - 2y = %s$, $d_3: x + y = %s$, $d_4: x = %s$. \\\\
            Tọa độ các giao điểm tương ứng: \\\\
            - $A$ là giao điểm của $d_1$ và $d_2 \\implies A(%s; %s)$. \\\\
            - $B$ là giao điểm của $d_2$ và $d_3 \\implies B(%s; %s)$. \\\\
            - $C$ là giao điểm của $d_3$ và $d_4 \\implies C(%s; %s)$. \\\\
            - $D$ là giao điểm của $d_4$ và $d_1 \\implies D(%s; %s)$. \\\\
            Miền nghiệm của hệ bất phương trình $(I)$ là miền tứ giác $ABCD$ (kể cả biên). %s \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-1,-1) rectangle (5,5);
            \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle (5,5);
            \\fill[white] (%s, %s) -- (%s, %s) -- (%s, %s) -- (%s, %s) -- cycle;
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (-1, %s) -- (5, %s);
            \\draw[black] (%s, -1) -- (%s, 5);
            \\draw[black] (0, -1) -- (0, 5);
            \\coordinate (A) at (%s,%s);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (%s,%s);
            \\coordinate (D) at (%s,%s);
            \\node at (A) [below] {$A$};
            \\node at (B) [right] {$B$};
            \\node at (C) [above right] {$C$};
            \\node at (D) [left] {$D$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\fill (D) circle (1.5pt);
            \\draw[->] (-1, 0) -- (5, 0) node[below] {$x$};
            \\draw[->] (0, -1) -- (0, 5) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (C1, C2, C3, X0,
                                xA, yA, xB, yB, xC, yC, xD, yD, eval_vdc,
                                round(xA_p, 2), round(yA_p, 2),
                                round(xB_p, 2), round(yB_p, 2),
                                round(xC_p, 2), round(yC_p, 2),
                                round(xD_p, 2), round(yD_p, 2),
                                round(l1_y_m1, 2), round(l1_y_5, 2),
                                round(l2_y_m1, 2), round(l2_y_5, 2),
                                round(l3_y_m1, 2), round(l3_y_5, 2),
                                round(l4_x, 2), round(l4_x, 2),
                                round(xA_p, 2), round(yA_p, 2),
                                round(xB_p, 2), round(yB_p, 2),
                                round(xC_p, 2), round(yC_p, 2),
                                round(xD_p, 2), round(yD_p, 2)))

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

