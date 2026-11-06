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


def bt_dang13_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # 1. Random tham số để tạo hàm số bậc nhất trên bậc nhất luôn nghịch biến
            # f(x) = (a*x + b) / (x - x0)
            x0 = randint(1, 3)  # Tiệm cận đứng x = x0
            a_val = randint(1, 3)
            # Để đạo hàm âm: a_val * (-x0) - b_val < 0 => b_val > -a_val * x0. Chọn b_val nguyên dương cho đẹp.
            b_val = randint(1, 4)

            # Định thức tử số của đạo hàm: delta = a*d - b*c = a*(-x0) - b
            delta = -a_val * x0 - b_val  # Chắc chắn âm

            # Định nghĩa các biểu thức hình thức
            tu_so = a_val * x + b_val
            mau_so = x - x0
            y_expr = tu_so / mau_so

            # Đạo hàm chính xác: f'(x) = delta / (x - x0)^2
            tu_dao_ham_dung = delta
            mau_dao_ham_dung = (x - x0)**2

            # Đạo hàm sai (đổi dấu định thức hoặc đổi mẫu số)
            tu_dao_ham_sai = -delta

            # 2. Tạo các biểu thức bậc hai cho câu c đảm bảo u(m) < v(m) và đều > x0
            # u(m) = m^2 + x0 + 1
            # v(m) = 2*m^2 - 2*m + x0 + 3
            # Hiệu v(m) - u(m) = m^2 - 2*m + 2 = (m - 1)^2 + 1 > 0
            u_str = "m^2 + %s" % (x0 + 1)
            v_str = "2m^2 - 2m + %s" % (x0 + 3)
            hieu_str = "m^2 - 2m + 2 = (m - 1)^2 + 1"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = %s$.''' 
                             % (latex(y_expr)))

            ########################################################################
            # Nhận biết (Mệnh đề a) ################################################
            # Các đáp án
            nb_da_1_d = '\\True $f\'(x) = \\frac{%s}{%s}$' % (latex(tu_dao_ham_dung), latex(mau_dao_ham_dung))
            nb_da_1_s = '$f\'(x) = \\frac{%s}{%s}$' % (latex(tu_dao_ham_sai), latex(mau_dao_ham_dung))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tập xác định: $\\mathscr{D} = \\mathbb{R} \\setminus \\{%s\\}$.\\\\
            Ta có: $f\'(x) = \\frac{%s}{%s} \\Rightarrow f\'(x) < 0 \\quad \\forall x \\in \\mathscr{D}$.\\\\
            Do đó mệnh đề này %s.''' 
                            % (latex(x0), latex(tu_dao_ham_dung), latex(mau_dao_ham_dung), 
                               "đúng" if nb_da_1 == nb_da_1_d else "sai"))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Mệnh đề b) ###############################################
            # Các đáp án
            th_da_1_d = '\\True Hàm số $f(x)$ nghịch biến trên khoảng $\\left(-\\infty; %s\\right)$' % (latex(x0))
            th_da_1_s = 'Hàm số $f(x)$ đồng biến trên khoảng $\\left(-\\infty; %s\\right)$' % (latex(x0))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Do $f\'(x) < 0$ với mọi $x \\in \\left(-\\infty; %s\\right)$ nên hàm số nghịch biến trên khoảng này.\\\\
            Do đó mệnh đề này %s.''' 
                            % (latex(x0), "đúng" if th_da_1 == th_da_1_d else "sai"))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Mệnh đề c) #################################################
            # Các đáp án
            vd_da_1_d = '\\True Với mọi số thực $m$ thì $f\\left(%s\\right) > f\\left(%s\\right)$' % (u_str, v_str)
            vd_da_1_s = 'Với mọi số thực $m$ thì $f\\left(%s\\right) < f\\left(%s\\right)$' % (u_str, v_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Hàm số nghịch biến trên từng khoảng xác định.\\\\
            Xét hai giá trị $u = %s$ và $v = %s$.\\\\
            Ta có: $u = m^2 + %s \\ge %s > %s$ và $v = 2(m-0,5)^2 + %s \\ge %s > %s$ với mọi $m$.\\\\
            Hiệu: $v - u = %s > 0, \\forall m \\Rightarrow v > u > %s$.\\\\
            Vì $u, v$ cùng thuộc khoảng xác định $\\left(%s; +\\infty\\right)$ và $u < v$, đồng thời hàm số nghịch biến trên khoảng này nên ta có $f\\left(u\\right) > f\\left(v\\right)$, tức là $f\\left(%s\\right) > f\\left(%s\\right)$ với mọi $m$.\\\\
            Do đó mệnh đề này %s.''' 
                            % (u_str, v_str, 
                               latex(x0 + 1), latex(x0 + 1), latex(x0),
                               latex(x0 + 2.5), latex(x0 + 2.5), latex(x0),
                               hieu_str, latex(x0),
                               latex(x0),
                               u_str, v_str,
                               "đúng" if vd_da_1 == vd_da_1_d else "sai"))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Mệnh đề d) #############################################
            # Các đáp án
            vdc_da_1_d = '\\True Hàm số $f(x)$ không có cực trị'
            vdc_da_1_s = 'Hàm số $f(x)$ đạt cực trị tại $x = %s$' % (latex(x0))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Do $f\'(x)$ không đổi dấu trên $\\mathbb{R} \\setminus \\{%s\\}$ nên hàm số không có cực trị.\\\\
            Do đó mệnh đề này %s.''' 
                             % (latex(x0), "đúng" if vdc_da_1 == vdc_da_1_d else "sai"))

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

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn đúng cấu trúc đề bài
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

