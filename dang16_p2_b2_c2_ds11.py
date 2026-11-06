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


def bt_dang16_p2_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            u1 = randint(2, 8)
            d = randint(2, 5)
            N = 20
            S_N = (N // 2) * (2 * u1 + (N - 1) * d)

            d_sai = d + random.choice([-2, -1, 1, 2])
            if d_sai <= 0:
                d_sai = d + 2

            k1 = 4
            u_k1 = u1 + (k1 - 1) * d
            u_k1_sai = u_k1 + random.choice([-3, -2, -1, 1, 2, 3])

            M = 10
            S_M = (M // 2) * (2 * u1 + (M - 1) * d)
            S_M_sai = S_M + random.choice([-15, -10, -5, 5, 10, 15])

            p = 8
            q_val = 4
            S_p = (p // 2) * (2 * u1 + (p - 1) * d)
            S_q = (q_val // 2) * (2 * u1 + (q_val - 1) * d)
            diff_S = S_p - S_q
            diff_S_sai = diff_S + random.choice([-10, -5, 5, 10])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho dãy cấp số cộng $(u_n)$ có $u_1 = %s$. Biết tổng %s số hạng đầu tiên bằng %s.'''
                             % (latex(u1), latex(N), latex(S_N)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Dãy số $(u_n)$ có $d = %s$' % latex(d)
            nb_da_1_s = 'Dãy số $(u_n)$ có $d = %s$' % latex(d_sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Công thức tính tổng $n$ số hạng đầu tiên của cấp số cộng là $S_n = \\frac{n[2u_1 + (n-1)d]}{2}$. \\\\
            Theo đề bài, ta có $S_{%s} = %s$, suy ra: \\\\
            $\\frac{%s \\cdot [2 \\cdot %s + (%s - 1)d]}{2} = %s \\Leftrightarrow %s \\cdot (%s + %sd) = %s \\Leftrightarrow %s + %sd = %s \\Leftrightarrow %sd = %s \\Leftrightarrow d = %s$. \\\\
            Vậy dãy số $(u_n)$ có $d = %s$.'''
                        % (latex(N), latex(S_N), latex(N), latex(u1), latex(N), latex(S_N),
                           latex(N // 2), latex(2 * u1), latex(N - 1), latex(S_N),
                           latex(2 * u1), latex(N - 1), latex(S_N // (N // 2)),
                           latex(N - 1), latex((S_N // (N // 2)) - 2 * u1), latex(d), latex(d)))

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
            th_da_1_d = '\\True Dãy số $(u_n)$ có $u_{%s} = %s$' % (latex(k1), latex(u_k1))
            th_da_1_s = 'Dãy số $(u_n)$ có $u_{%s} = %s$' % (latex(k1), latex(u_k1_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Số hạng thứ %s của cấp số cộng là: \\\\
            $u_{%s} = u_1 + %sd = %s + %s \\cdot %s = %s$.'''
                        % (latex(k1), latex(k1), latex(k1 - 1), latex(u1), latex(k1 - 1), latex(d), latex(u_k1)))

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
            vd_da_1_d = '\\True Dãy số $(u_n)$ có $S_{%s} = %s$' % (latex(M), latex(S_M))
            vd_da_1_s = 'Dãy số $(u_n)$ có $S_{%s} = %s$' % (latex(M), latex(S_M_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng %s số hạng đầu tiên của dãy số là: \\\\
            $S_{%s} = \\frac{%s \\cdot [2u_1 + %sd]}{2} = \\frac{%s \\cdot [2 \\cdot %s + %s \\cdot %s]}{2} = %s \\cdot (%s + %s) = %s$.'''
                        % (latex(M), latex(M), latex(M), latex(M - 1), latex(M), latex(u1), latex(M - 1), latex(d),
                           latex(M // 2), latex(2 * u1), latex((M - 1) * d), latex(S_M)))

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
            vdc_da_1_d = '\\True Dãy số $(u_n)$ có hiệu $S_{%s} - S_{%s} = %s$' % (latex(p), latex(q_val), latex(diff_S))
            vdc_da_1_s = 'Dãy số $(u_n)$ có hiệu $S_{%s} - S_{%s} = %s$' % (latex(p), latex(q_val), latex(diff_S_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có: \\\\
            $S_{%s} = \\frac{%s \\cdot [2u_1 + %sd]}{2} = \\frac{%s \\cdot [2 \\cdot %s + %s \\cdot %s]}{2} = %s \\cdot (%s + %s) = %s$. \\\\
            $S_{%s} = \\frac{%s \\cdot [2u_1 + %sd]}{2} = \\frac{%s \\cdot [2 \\cdot %s + %s \\cdot %s]}{2} = %s \\cdot (%s + %s) = %s$. \\\\
            Suy ra $S_{%s} - S_{%s} = %s - %s = %s$.'''
                        % (latex(p), latex(p), latex(p - 1), latex(p), latex(u1), latex(p - 1), latex(d), latex(p // 2), latex(2 * u1), latex((p - 1) * d), latex(S_p),
                           latex(q_val), latex(q_val), latex(q_val - 1), latex(q_val), latex(u1), latex(q_val - 1), latex(d), latex(q_val // 2), latex(2 * u1), latex((q_val - 1) * d), latex(S_q),
                           latex(p), latex(q_val), latex(S_p), latex(S_q), latex(diff_S)))

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

