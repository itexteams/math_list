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


def bt_dang18_p2_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            u1 = randint(-10, -3)
            d = randint(2, 5)

            n1 = randint(30, 45)
            val1 = u1 + (n1 - 1) * d
            n1_sai = n1 + random.choice([-3, -2, -1, 1, 2, 3])

            k2 = randint(3, 6)
            u_k2 = u1 + (k2 - 1) * d
            u_k2_sai = u_k2 + random.choice([-4, -3, -1, 1, 3, 4])

            N3 = randint(8, 12)
            S_N3 = (N3 * (2 * u1 + (N3 - 1) * d)) // 2
            S_N3_sai = S_N3 + random.choice([-30, -20, -10, 10, 20, 30])

            k0 = (-u1) // d + 2
            k0_sai = k0 + random.choice([-2, -1, 1, 2])
            if k0_sai <= 1:
                k0_sai = k0 + 2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho cấp số cộng $(u_n)$ có $u_1 = %s$, công sai $d = %s$.'''
                             % (latex(u1), latex(d)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số %s là số hạng thứ %s của cấp số cộng' % (latex(val1), latex(n1))
            nb_da_1_s = 'Số %s là số hạng thứ %s của cấp số cộng' % (latex(val1), latex(n1_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Giả sử số %s là số hạng thứ $n$ của cấp số cộng. \\\\
            Ta có $u_n = u_1 + (n-1)d \\Leftrightarrow %s = %s + (n-1) \\cdot %s$. \\\\
            $\\Leftrightarrow (n-1) \\cdot %s = %s \\Leftrightarrow n - 1 = %s \\Leftrightarrow n = %s$. \\\\
            Vậy số %s là số hạng thứ %s của cấp số cộng.'''
                        % (latex(val1), latex(val1), latex(u1), latex(d),
                           latex(d), latex(val1 - u1), latex((val1 - u1) // d), latex(n1),
                           latex(val1), latex(n1)))

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
            th_da_1_d = '\\True Số hạng thứ %s của cấp số cộng bằng %s' % (latex(k2), latex(u_k2))
            th_da_1_s = 'Số hạng thứ %s của cấp số cộng bằng %s' % (latex(k2), latex(u_k2_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Số hạng thứ %s của cấp số cộng là: \\\\
            $u_{%s} = u_1 + %sd = %s + %s \\cdot %s = %s$.'''
                        % (latex(k2), latex(k2), latex(k2 - 1), latex(u1), latex(k2 - 1), latex(d), latex(u_k2)))

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
            vd_da_1_d = '\\True Tổng %s số hạng đầu tiên của cấp số cộng bằng %s' % (latex(N3), latex(S_N3))
            vd_da_1_s = 'Tổng %s số hạng đầu tiên của cấp số cộng bằng %s' % (latex(N3), latex(S_N3_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng %s số hạng đầu tiên của cấp số cộng là: \\\\
            $S_{%s} = \\frac{%s \\cdot [2u_1 + %sd]}{2} = \\frac{%s \\cdot [2 \\cdot (%s) + %s \\cdot %s]}{2} = %s$.'''
                        % (latex(N3), latex(N3), latex(N3), latex(N3 - 1),
                           latex(N3), latex(u1), latex(N3 - 1), latex(d), latex(S_N3)))

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
            vdc_da_1_d = '\\True Kể từ số hạng thứ %s thì các số hạng của cấp số cộng đều nhận giá trị dương' % latex(k0)
            vdc_da_1_s = 'Kể từ số hạng thứ %s thì các số hạng của cấp số cộng đều nhận giá trị dương' % latex(k0_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Xử lý trình bày bất phương trình cho lời giải
            if (-u1) % d == 0:
                ineq_str = "(n-1) \\cdot %s > %s \\Leftrightarrow n - 1 > %s \\Leftrightarrow n > %s" % (
                    latex(d), latex(-u1), latex((-u1) // d), latex(1 + (-u1) // d)
                )
            else:
                frac_val = round(-u1 / d, 2)
                frac_str = str(frac_val).replace('.', ',')
                n_val = round(1 + -u1 / d, 2)
                n_str = str(n_val).replace('.', ',')
                ineq_str = "(n-1) \\cdot %s > %s \\Leftrightarrow n - 1 > \\frac{%s}{%s} \\approx %s \\Leftrightarrow n > %s" % (
                    latex(d), latex(-u1), latex(-u1), latex(d), frac_str, n_str
                )

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số hạng tổng quát của cấp số cộng là $u_n = u_1 + (n-1)d = %s + (n-1) \\cdot %s$. \\\\
            Để $u_n > 0$ thì $%s + (n-1) \\cdot %s > 0 \\Leftrightarrow %s$. \\\\
            Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$. \\\\
            Mặt khác vì công sai $d = %s > 0$ nên dãy số $(u_n)$ là dãy tăng. \\\\
            Do đó kể từ số hạng thứ %s thì các số hạng của cấp số cộng đều nhận giá trị dương.'''
                        % (latex(u1), latex(d),
                           latex(u1), latex(d), ineq_str,
                           latex(k0), latex(d), latex(k0)))

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

