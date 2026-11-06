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


def bt_dang17_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random giữa 2 hàm số lượng giác tương tự nhau để đảm bảo đề bài luôn phong phú
            mode = random.choice([1, 2])

            if mode == 1:
                # Hàm số y = x/2 - sin^2(x)
                ten_ham = "\\frac{x}{2} - \\sin^2 x"
                f_x = x/2 - sin(x)**2
                dao_ham = "\\frac{1}{2} - \\sin 2x"
                sin_val = "\\frac{1}{2}"

                # Nghiệm trên (0; pi)
                x1_str = "\\frac{\\pi}{12}"
                x2_str = "\\frac{5\\pi}{12}"

                # Giá trị cực trị
                y1_str = "\\frac{\\pi}{24} - \\frac{2-\\sqrt{3}}{4}"
                y2_str = "\\frac{5\\pi}{24} - \\frac{2+\\sqrt{3}}{4}"

                # Giá trị biên
                y_0 = "0"
                y_pi = "\\frac{\\pi}{2}"

                # Các khoảng đồng biến / nghịch biến
                db_interval_1 = "\\left(0; \\frac{\\pi}{12}\\right)"
                nb_interval = "\\left(\\frac{\\pi}{12}; \\frac{5\\pi}{12}\\right)"
                db_interval_2 = "\\left(\\frac{5\\pi}{12}; \\pi\\right)"

                # Thiết lập đáp án Đúng / Sai
                nb_da_d = "\\True Hàm số nghịch biến trên khoảng $\\left(\\frac{\\pi}{12}; \\frac{5\\pi}{12}\\right)$"
                nb_da_s = "Hàm số nghịch biến trên khoảng $\\left(\\frac{5\\pi}{12}; \\pi\\right)$"

                th_da_d = "\\True Hàm số có hai điểm cực trị"
                th_da_s = "Hàm số có ba điểm cực trị"

                vd_da_d = "\\True Giá trị cực tiểu của hàm số là $\\frac{5\\pi}{24} - \\frac{2+\\sqrt{3}}{4}$"
                vd_da_s = "Giá trị cực tiểu của hàm số là $\\frac{\\pi}{24} - \\frac{2-\\sqrt{3}}{4}$"

                vdc_da_d = "\\True Hàm số đồng biến trên khoảng $\\left(0; \\frac{\\pi}{12}\\right)$"
                vdc_da_s = "Hàm số đồng biến trên khoảng $\\left(\\frac{\\pi}{12}; \\frac{5\\pi}{12}\\right)$"

            else:
                # Hàm số y = x/2 - cos^2(x)
                ten_ham = "\\frac{x}{2} - \\cos^2 x"
                f_x = x/2 - cos(x)**2
                dao_ham = "\\frac{1}{2} + \\sin 2x"
                sin_val = "-\\frac{1}{2}"

                # Nghiệm trên (0; pi)
                x1_str = "\\frac{7\\pi}{12}"
                x2_str = "\\frac{11\\pi}{12}"

                # Giá trị cực trị
                y1_str = "\\frac{7\\pi}{24} - \\frac{2-\\sqrt{3}}{4}"
                y2_str = "\\frac{11\\pi}{24} - \\frac{2+\\sqrt{3}}{4}"

                # Giá trị biên
                y_0 = "-1"
                y_pi = "\\frac{\\pi}{2} - 1"

                # Các khoảng đồng biến / nghịch biến
                db_interval_1 = "\\left(0; \\frac{7\\pi}{12}\\right)"
                nb_interval = "\\left(\\frac{7\\pi}{12}; \\frac{11\\pi}{12}\\right)"
                db_interval_2 = "\\left(\\frac{11\\pi}{12}; \\pi\\right)"

                # Thiết lập đáp án Đúng / Sai
                nb_da_d = "\\True Hàm số nghịch biến trên khoảng $\\left(\\frac{7\\pi}{12}; \\frac{11\\pi}{12}\\right)$"
                nb_da_s = "Hàm số nghịch biến trên khoảng $\\left(\\frac{11\\pi}{12}; \\pi\\right)$"

                th_da_d = "\\True Hàm số có hai điểm cực trị"
                th_da_s = "Hàm số không có cực trị"

                vd_da_d = "\\True Giá trị cực tiểu của hàm số là $\\frac{11\\pi}{24} - \\frac{2+\\sqrt{3}}{4}$"
                vd_da_s = "Giá trị cực tiểu của hàm số là $\\frac{7\\pi}{24} - \\frac{2-\\sqrt{3}}{4}$"

                vdc_da_d = "\\True Hàm số đồng biến trên khoảng $\\left(0; \\frac{7\\pi}{12}\\right)$"
                vdc_da_s = "Hàm số đồng biến trên khoảng $\\left(\\frac{7\\pi}{12}; \\frac{11\\pi}{12}\\right)$"


            # Đưa vào danh sách để xáo trộn
            list_nb_da = [nb_da_d, nb_da_s]
            list_th_da = [th_da_d, th_da_s]
            list_vd_da = [vd_da_d, vd_da_s]
            list_vdc_da = [vdc_da_d, vdc_da_s]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét hàm số $y = %s$ trên khoảng $(0; \\pi)$.''' % ten_ham)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da = random.choice(list_nb_da)
                th_da = random.choice(list_th_da)
                vd_da = random.choice(list_vd_da)
                vdc_da = random.choice(list_vdc_da)

                answers = [nb_da, th_da, vd_da, vdc_da]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Sinh lời giải động dựa trên đáp án được chọn ngẫu nhiên
            if '\\True' in nb_da:
                loigiai_nb = 'Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $%s$ là mệnh đề đúng.' % nb_interval
            else:
                loigiai_nb = 'Dựa vào bảng biến thiên, hàm số đồng biến trên khoảng $%s$, do đó mệnh đề nghịch biến trên khoảng này là mệnh đề sai.' % db_interval_2

            if '\\True' in th_da:
                loigiai_th = 'Hàm số có hai điểm cực trị là mệnh đề đúng.'
            else:
                loigiai_th = 'Hàm số có đúng hai điểm cực trị, do đó mệnh đề trên là mệnh đề sai.'

            if '\\True' in vd_da:
                loigiai_vd = 'Giá trị cực tiểu của hàm số là $%s$ là mệnh đề đúng.' % y2_str
            else:
                loigiai_vd = 'Giá trị cực tiểu của hàm số phải là $%s$, do đó mệnh đề trên là mệnh đề sai.' % y2_str

            if '\\True' in vdc_da:
                loigiai_vdc = 'Hàm số đồng biến trên khoảng $%s$ là mệnh đề đúng.' % db_interval_1
            else:
                loigiai_vdc = 'Trên khoảng $%s$ hàm số nghịch biến, do đó mệnh đề đồng biến trên khoảng này là mệnh đề sai.' % nb_interval

            # Gán lại vào list và xáo trộn
            list_nb_1 = [nb_da]
            list_th_1 = [th_da]
            list_vd_1 = [vd_da]
            list_vdc_1 = [vdc_da]

            list_nb_2 = [loigiai_nb]
            list_th_2 = [loigiai_th]
            list_vd_2 = [loigiai_vd]
            list_vdc_2 = [loigiai_vdc]

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

            # Khối Lời giải chung (Đạo hàm, Bảng biến thiên TikZ không vạch kẻ đứng ở dòng đạo hàm)
            loigiai_chung = ('''Hàm số xác định trên khoảng $(0; \\pi)$. \\\\
            Ta có $y' = %s$. \\\\
            $y' = 0 \\Leftrightarrow \\sin 2x = %s \\Leftrightarrow \\left[\\begin{array}{l} 2x = \\arcsin\\left(%s\\right) + k2\\pi \\\\ 2x = \\pi - \\arcsin\\left(%s\\right) + k2\\pi \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} x = %s + k\\pi \\\\ x = %s + k\\pi \\end{array}\\right. , (k \\in \\mathbb{Z})$. \\\\
            Phương trình $y' = 0$ có đúng 2 nghiệm $x = %s$ và $x = %s$ trên khoảng $(0; \\pi)$. \\\\
            Bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\def\\w{1.5}
            \\def\\c{2.2}
            \\draw (0,0) rectangle (\\w+4*\\c, -4.5);
            \\draw (0,-1) -- (\\w+4*\\c, -1);
            \\draw (0,-2) -- (\\w+4*\\c, -2);
            \\draw (\\w,0) -- (\\w,-4.5);
            \\node at (\\w/2, -0.5) {$x$};
            \\node at (\\w/2, -1.5) {$y'$};
            \\node at (\\w/2, -3.25) {$y$};
            \\node at (\\w+0.5*\\c, -0.5) {$0$};
            \\node at (\\w+1.5*\\c, -0.5) {$%s$};
            \\node at (\\w+2.5*\\c, -0.5) {$%s$};
            \\node at (\\w+3.5*\\c, -0.5) {$\\pi$};
            \\node at (\\w+1.5*\\c, -1.5) {$0$};
            \\node at (\\w+2.5*\\c, -1.5) {$0$};
            \\node at (\\w+0.75*\\c, -1.5) {$+$};
            \\node at (\\w+2.0*\\c, -1.5) {$-$};
            \\node at (\\w+3.0*\\c, -1.5) {$+$};
            \\node (A) at (\\w+0.5*\\c, -4) {$%s$};
            \\node (B) at (\\w+1.5*\\c, -2.5) {$%s$};
            \\node (C) at (\\w+2.5*\\c, -4) {$%s$};
            \\node (D) at (\\w+3.5*\\c, -2.5) {$%s$};
            \\draw[->] (A) -- (B);
            \\draw[->] (B) -- (C);
            \\draw[->] (C) -- (D);
            \\end{tikzpicture}
            \\end{center}''' % (dao_ham, sin_val, sin_val, sin_val, x1_str, x2_str, x1_str, x2_str, 
                                   x1_str, x2_str, y_0, y1_str, y2_str, y_pi))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n' +
                str(loigiai_chung) + '\n' +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

