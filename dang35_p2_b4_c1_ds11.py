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


def bt_dang35_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            goc_list = [30, 45, 60]
            goc = random.choice(goc_list)

            if goc == 30:
                goc_rad = "\\frac{\\pi}{6}"
                sin_val = "\\frac{1}{2}"
                cos_val = "\\frac{\\sqrt{3}}{2}"
                sin2_val = "\\frac{2 - \\sqrt{3}}{4}"
                mon_val = 60
                mon_rad = "\\frac{\\pi}{3}"
                check_a = False
            elif goc == 45:
                goc_rad = "\\frac{\\pi}{4}"
                sin_val = "\\frac{\\sqrt{2}}{2}"
                cos_val = "\\frac{\\sqrt{2}}{2}"
                sin2_val = "\\frac{2 - \\sqrt{2}}{4}"
                mon_val = 90
                mon_rad = "\\frac{\\pi}{2}"
                check_a = False
            else:
                goc_rad = "\\frac{\\pi}{3}"
                sin_val = "\\frac{\\sqrt{3}}{2}"
                cos_val = "\\frac{1}{2}"
                sin2_val = "\\frac{1}{4}"
                mon_val = 120
                mon_rad = "\\frac{2\\pi}{3}"
                check_a = True

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho vòng tròn lượng giác như hình vẽ, $M$ và $N$ đối xứng qua trục và $\\widehat{MOx} = %s^\\circ$.
            \\begin{center}
            \\begin{tikzpicture}[scale=1.5,>=stealth, line width=1pt]
            \\draw[->] (-1.5,0) -- (1.5,0) node[above] {$x$};
            \\draw[->] (0,-1.5) -- (0,1.5) node[right] {$y$};
            \\draw (0,0) circle (1);
            \\node[below left] at (0,0) {$O$};
            \\node[above left] at (-1,0) {$-1$};
            \\node[below right] at (1,0) {$1$};
            \\node[below right] at (0,-1) {$-1$};
            \\node[above right] at (0,1) {$1$};
            \\draw (0,0) -- (%s:%s) node[above right] {$M$};
            \\draw (0,0) -- (-%s:%s) node[below right] {$N$};
            \\draw[dashed] (%s:%s) -- (-%s:%s);
            \\foreach \\x in {-1,1} \\draw (\\x,0.05) -- (\\x,-0.05);
            \\foreach \\y in {-1,1} \\draw (0.05,\\y) -- (-0.05,\\y);
            \\end{tikzpicture}
            \\end{center}''' % (goc, goc, 1, goc, 1, goc, 1, goc, 1))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            if check_a:
                nb_da_1_d = '\\True $\\widehat{MON} > \\frac{\\pi}{2}$ radian'
                nb_da_1_s = '$\\widehat{MON} < \\frac{\\pi}{2}$ radian'
            else:
                nb_da_1_d = '$\\widehat{MON} > \\frac{\\pi}{2}$ radian'
                nb_da_1_s = '\\True $\\widehat{MON} \\le \\frac{\\pi}{2}$ radian'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\widehat{MON} = 2\\widehat{MOx} = 2 \\cdot %s^\\circ = %s^\\circ = %s$ radian. Từ đó suy ra tính đúng sai của khẳng định.''' % (goc, mon_val, mon_rad))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Điểm $M$ biểu diễn nghiệm của phương trình $\\sin x = %s$' % (sin_val)
            th_da_1_s = 'Điểm $M$ biểu diễn nghiệm của phương trình $\\sin x = %s$' % (cos_val)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Điểm $M$ thuộc góc phần tư thứ nhất, biểu diễn góc lượng giác có số đo $\\alpha = %s^\\circ$. Khi đó tung độ của điểm $M$ là $\\sin \\alpha = \\sin %s^\\circ = %s$. Vậy điểm $M$ biểu diễn nghiệm của phương trình $\\sin x = %s$.''' % (goc, goc, sin_val, sin_val))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = 'Giả sử $M, N$ di động ở nửa bên phải vòng tròn lượng giác, khi đó diện tích tam giác $MON$ lớn nhất khi $\\widehat{MON} = 60^\\circ$'
            vd_da_1_s = '\\True Giả sử $M, N$ di động ở nửa bên phải vòng tròn lượng giác, khi đó diện tích tam giác $MON$ lớn nhất khi $\\widehat{MON} = 90^\\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Diện tích tam giác $MON$ là $S = \\frac{1}{2} OM \\cdot ON \\cdot \\sin \\widehat{MON} = \\frac{1}{2} \\sin \\widehat{MON} \\le \\frac{1}{2}$. Dấu $=$ xảy ra khi $\\sin \\widehat{MON} = 1 \\Leftrightarrow \\widehat{MON} = 90^\\circ$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Hai điểm $M$ và $N$ biểu diễn đầy đủ nghiệm của phương trình $\\sin^2 \\frac{x}{2} = %s$' % (sin2_val)
            vdc_da_1_s = 'Hai điểm $M$ và $N$ biểu diễn đầy đủ nghiệm của phương trình $\\sin^2 \\frac{x}{2} = %s$' % (sin_val)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\sin^2 \\frac{x}{2} = \\frac{1 - \\cos x}{2}$. Hai điểm $M, N$ có cùng hoành độ là $\\cos x = \\cos %s^\\circ = %s$. Do đó, hai điểm $M, N$ biểu diễn nghiệm của phương trình $\\sin^2 \\frac{x}{2} = \\frac{1 - %s}{2} = %s$.''' % (goc, cos_val, cos_val, sin2_val))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

