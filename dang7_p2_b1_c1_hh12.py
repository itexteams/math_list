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


def bt_dang7_p2_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên
            k = random.randint(1, 4)
            if k == 1:
                k_str = "a"
                cd_str = "a\\sqrt{2}"
                k_sq_str = "a^2"
                k_sq_half_str = "\\frac{a^2}{2}"
                neg_k_sq_half_str = "-\\frac{a^2}{2}"
            else:
                k_str = f"{k}a"
                cd_str = f"{k}a\\sqrt{{2}}"
                k_sq_str = f"{k**2}a^2"
                if (k**2) % 2 == 0:
                    k_sq_half_str = f"{(k**2)//2}a^2"
                    neg_k_sq_half_str = f"-{(k**2)//2}a^2"
                else:
                    k_sq_half_str = f"\\frac{{{k**2}a^2}}{{2}}"
                    neg_k_sq_half_str = f"-\\frac{{{k**2}a^2}}{{2}}"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện $ABCD$ có $G$ là trọng tâm tam giác $BCD$, $AB = AC = AD = BD = BC = %s$, $CD = %s$.''' % (k_str, cd_str))

            # Code TikZ cho phần lời giải
            tikz_code = '''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line width=1pt,, line cap=round]
                \\coordinate (B) at (0,0);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at (1.5,-1.5);
                \\coordinate (A) at (2,3.5);
                \\draw[dashed] (B) -- (D);
                \\draw (A) -- (B) node[midway, above left] {$%s$};
                \\draw (A) -- (C) node[midway, left] {$%s$};
                \\draw (A) -- (D) node[midway, above right] {$%s$};
                \\draw (B) -- (C) node[midway, below left] {$%s$};
                \\draw (C) -- (D) node[midway, below right] {$%s$};
                \\node at (2, 0.2) {$%s$};
                \\fill (A) circle (0.5pt) node[above] {$A$};
                \\fill (B) circle (0.5pt) node[left] {$B$};
                \\fill (C) circle (0.5pt) node[below] {$C$};
                \\fill (D) circle (0.5pt) node[right] {$D$};
            \\end{tikzpicture}
            \\end{center}''' % (k_str, k_str, k_str, k_str, cd_str, k_str)

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True $\\overrightarrow{GB} + \\overrightarrow{GC} + \\overrightarrow{GD} = \\vec{0}$'
            nb_da_1_s = '$\\overrightarrow{GB} + \\overrightarrow{GC} + \\overrightarrow{GD} = 0$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $G$ là trọng tâm tam giác $BCD$ nên $\\overrightarrow{GB} + \\overrightarrow{GC} + \\overrightarrow{GD} = \\vec{0}$.''')
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = %s$' % (k_sq_half_str)
            th_da_1_s = '$\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = %s$' % (k_sq_str)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì $\\Delta ABC$ đều nên áp dụng công thức tích vô hướng cho hai vectơ $\\overrightarrow{AB}, \\overrightarrow{AC}$ ta có:\\\\
            $\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = AB \\cdot AC \\cdot \\cos(\\overrightarrow{AB}, \\overrightarrow{AC}) = AB \\cdot AC \\cdot \\cos(\\widehat{BAC}) = %s \\cdot %s \\cdot \\cos 60^\\circ = %s$.''' % (k_str, k_str, k_sq_half_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\overrightarrow{AB} + \\overrightarrow{CD} = \\overrightarrow{AD} + \\overrightarrow{CB}$'
            vd_da_1_s = '$\\overrightarrow{AB} + \\overrightarrow{CD} = \\overrightarrow{AC} + \\overrightarrow{DB}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $\\overrightarrow{AB} + \\overrightarrow{CD} = (\\overrightarrow{AD} + \\overrightarrow{DB}) + \\overrightarrow{CD} = \\overrightarrow{AD} + (\\overrightarrow{CD} + \\overrightarrow{DB}) = \\overrightarrow{AD} + \\overrightarrow{CB}$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Góc giữa hai vectơ $\\overrightarrow{AC}$ và $\\overrightarrow{BD}$ bằng $120^\\circ$'
            vdc_da_1_s = 'Góc giữa hai vectơ $\\overrightarrow{AC}$ và $\\overrightarrow{BD}$ bằng $60^\\circ$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\overrightarrow{AB} \\cdot \\overrightarrow{BD} = -\\overrightarrow{BA} \\cdot \\overrightarrow{BD} = -\\frac{1}{2}(AB^2 + BD^2 - AD^2) = -\\frac{1}{2}\\left((%s)^2 + (%s)^2 - (%s)^2\\right) = %s$. \\\\
            Mặt khác tam giác $BCD$ có $BC = BD = %s, CD = %s$ \\\\ Suy ra $BC^2 + BD^2 = CD^2 \\Rightarrow \\overrightarrow{BC} \\cdot \\overrightarrow{BD} = 0$. \\\\
            $\\cos(\\overrightarrow{AC}, \\overrightarrow{BD}) = \\frac{\\overrightarrow{AC} \\cdot \\overrightarrow{BD}}{|\\overrightarrow{AC}| \\cdot |\\overrightarrow{BD}|} = \\frac{(\\overrightarrow{AB} + \\overrightarrow{BC}) \\cdot \\overrightarrow{BD}}{%s} = \\frac{\\overrightarrow{AB} \\cdot \\overrightarrow{BD} + \\overrightarrow{BC} \\cdot \\overrightarrow{BD}}{%s} = \\frac{%s + 0}{%s} = -\\frac{1}{2}$. \\\\
            Vậy $(\\overrightarrow{AC}, \\overrightarrow{BD}) = 120^\\circ$.''' % (k_str, k_str, k_str, neg_k_sq_half_str, k_str, cd_str, k_sq_str, k_sq_str, neg_k_sq_half_str, k_sq_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\loigiai{ \n' + tikz_code + '\n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace ('\\frac','\\dfrac')
            return content

