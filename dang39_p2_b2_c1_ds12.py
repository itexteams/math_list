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


def bt_dang39_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bộ dữ liệu ngẫu nhiên (M: Tối đa, A: Chi phí cố định, B: Chi phí mỗi bình, C: Hệ số bảo dưỡng, x_test: test câu thông hiểu, x_opt: Số bình tối ưu)
            cases = [
                (30, 10, 1.4, 0.025, 10, 20),
                (40, 16, 1.5, 0.04, 10, 20),
                (30, 12, 1.2, 0.12, 5, 10),
                (40, 18, 2.1, 0.02, 10, 30),
                (50, 20, 1.8, 0.05, 10, 20)
            ]
            M_val, A_val, B_val, C_coeff, x_test_val, x_opt_val = random.choice(cases)

            def format_num(num):
                # Làm tròn số đến 2 hoặc 3 chữ số thập phân để tránh lỗi floating-point
                num = round(float(num), 3) 
                if num.is_integer():
                    num = int(num)
                return str(num).replace('.', ',')

            str_M = format_num(M_val)
            str_A = format_num(A_val)
            str_B = format_num(B_val)
            str_C = format_num(C_coeff)
            str_xtest = format_num(x_test_val)
            str_xopt = format_num(x_opt_val)

            # Tính toán các giá trị cho đáp án
            c_xtest = C_coeff * x_test_val**2 + B_val * x_test_val + A_val
            c_bar_xtest = c_xtest / x_test_val
            str_cbar_xtest = format_num(c_bar_xtest)
            str_cbar_xtest_wrong = format_num(round(c_bar_xtest / 2, 2))

            min_cbar = C_coeff * x_opt_val + B_val + A_val / x_opt_val
            str_min_cbar = format_num(min_cbar)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một cơ sở sản xuất gốm sản xuất được tối đa %s bình gốm mỗi ngày. Biết rằng nếu mỗi ngày cơ sở sản xuất được $x$ bình gốm thì phải trả các chi phí sau: %s triệu đồng chi phí cố định; %s triệu đồng cho mỗi bình gốm và $%s x^2$ triệu đồng chi phí bảo dưỡng máy móc.''' 
                             % (str_M, str_A, str_B, str_C))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chi phí để sản xuất $x$ bình gốm là $C(x)=%s x^2 + %s x + %s$ (triệu đồng)' % (str_C, str_B, str_A)
            nb_da_1_s = 'Chi phí để sản xuất $x$ bình gốm là $C(x)=%s x^2 + %s x$ (triệu đồng)' % (str_C, str_B)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Chi phí để sản xuất $x$ bình gốm bằng tổng chi phí cố định, chi phí sản xuất mỗi bình và chi phí bảo dưỡng.\\\\
            Vậy $C(x) = %s x^2 + %s x + %s$ (triệu đồng).''' % (str_C, str_B, str_A))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Chi phí trung bình để sản xuất mỗi bình gốm là $\\overline{C} = %s x + %s + \\frac{%s}{x}$ (triệu đồng)' % (str_C, str_B, str_A)
            th_da_1_s = 'Chi phí trung bình để sản xuất mỗi bình gốm là $\\overline{C} = %s x + \\frac{%s}{x}$ (triệu đồng)' % (str_C, str_A)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Chi phí trung bình để sản xuất mỗi bình gốm được tính theo công thức:\\\\
            $\\overline{C} = \\frac{C(x)}{x} = \\frac{%s x^2 + %s x + %s}{x} = %s x + %s + \\frac{%s}{x}$ (triệu đồng).''' 
                            % (str_C, str_B, str_A, str_C, str_B, str_A))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Khi cơ sở sản xuất %s bình gốm thì chi phí trung bình để sản xuất mỗi bình là %s triệu đồng' % (str_xtest, str_cbar_xtest)
            vd_da_1_s = 'Khi cơ sở sản xuất %s bình gốm thì chi phí trung bình để sản xuất mỗi bình là %s triệu đồng' % (str_xtest, str_cbar_xtest_wrong)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $x = %s$ vào công thức chi phí trung bình ta được:\\\\
            $\\overline{C}(%s) = %s \\cdot %s + %s + \\frac{%s}{%s} = %s$ (triệu đồng).''' 
                            % (str_xtest, str_xtest, str_C, str_xtest, str_B, str_A, str_xtest, str_cbar_xtest))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Để chi phí trung bình sản xuất mỗi bình gốm là ít nhất thì cơ sở phải sản xuất %s bình gốm mỗi ngày' % (str_xopt)
            vdc_da_1_s = 'Để chi phí trung bình sản xuất mỗi bình gốm là ít nhất thì cơ sở phải sản xuất %s bình gốm mỗi ngày' % (format_num(x_opt_val + 5))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét hàm số $f(x) = %s x + %s + \\frac{%s}{x}$ trên khoảng $(0; %s]$.\\\\
            Ta có $f'(x) = %s - \\frac{%s}{x^2}$.\\\\
            $f'(x) = 0 \\Leftrightarrow %s - \\frac{%s}{x^2} = 0 \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ (do $x > 0$).\\\\
            Bảng biến thiên: \\\\
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$f'(x)$/0.7,$f(x)$/2.1}
            {$0$,$%s$,$%s$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/$+\\infty$,-/{$%s$},+/$f(%s)$} 
            \\end{tikzpicture} \\\\
            Dựa vào bảng biến thiên, chi phí trung bình đạt giá trị nhỏ nhất khi $x = %s$.\\\\
            Vậy để chi phí trung bình sản xuất mỗi bình gốm là ít nhất thì cơ sở phải sản xuất %s bình gốm mỗi ngày.''' 
            % (str_C, str_B, str_A, str_M, 
               str_C, str_A, 
               str_C, str_A, format_num(A_val/C_coeff), str_xopt, 
               str_xopt, str_M, 
               str_min_cbar, str_M, 
               str_xopt, 
               str_xopt))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

