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


def bt_dang21_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các hệ số của bất phương trình ax - y <= c
            a = random.choice([2, 3, 4])
            c = random.choice([1, 2, 3])

            expr_left = a * x - y
            expr_eq = a * x - y - c

            # Test điểm cho câu a
            xa = random.choice([1, 2])
            ya = random.choice([-1, -2])
            val_a = a * xa - ya
            is_sol_a = val_a <= c

            # Điểm O(0,0) cho câu b
            val_b = a * 0 - 0
            is_sol_b = val_b <= c

            # Test điểm cho câu c
            xc = random.choice([-2, -3])
            yc = random.choice([3, 4])
            val_c = a * xc - yc
            is_sol_c = val_c <= c

            # Test điểm cho câu d: (m, yd)
            yd = random.choice([5, 7, 9])
            # a*m - yd <= c => a*m <= c + yd => m <= (c + yd)/a
            max_m_exact = (c + yd) / a
            max_m_int = math.floor(max_m_exact)
            # Số giá trị nguyên dương
            num_m = max_m_int if max_m_int > 0 else 0


            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $%s x - y \\le %s$.''' 
                             % (a, c))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            if is_sol_a:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của bất phương trình đã cho' % (xa, ya)
                nb_da_1_s = 'Cặp số $(%s; %s)$ không là nghiệm của bất phương trình đã cho' % (xa, ya)
            else:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ không là nghiệm của bất phương trình đã cho' % (xa, ya)
                nb_da_1_s = 'Cặp số $(%s; %s)$ là nghiệm của bất phương trình đã cho' % (xa, ya)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            cmp_a = "\\le" if is_sol_a else ">"
            res_a = "là một nghiệm" if is_sol_a else "không là nghiệm"
            loigiai_nb_1 = ('''Thay $x = %s, y = %s$ vào vế trái của bất phương trình ta được: \\\\
            $%s \\cdot %s - (%s) = %s$. \\\\
            Vì $%s %s %s$ nên cặp số $(%s; %s)$ %s của bất phương trình.'''
                            % (xa, ya, a, xa, ya, val_a, val_a, cmp_a, c, xa, ya, res_a))

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
            if is_sol_b:
                th_da_1_d = '\\True Gốc tọa độ $O$ thuộc miền nghiệm của bất phương trình'
                th_da_1_s = 'Gốc tọa độ $O$ không thuộc miền nghiệm của bất phương trình'
            else:
                th_da_1_d = '\\True Gốc tọa độ $O$ không thuộc miền nghiệm của bất phương trình'
                th_da_1_s = 'Gốc tọa độ $O$ thuộc miền nghiệm của bất phương trình'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            cmp_b = "\\le" if is_sol_b else ">"
            res_b = "thuộc" if is_sol_b else "không thuộc"
            loigiai_th_1 = ('''Gốc tọa độ $O$ có tọa độ $(0; 0)$. \\\\
            Thay $x = 0, y = 0$ vào bất phương trình ta được: $%s \\cdot 0 - 0 = %s$. \\\\
            Vì $%s %s %s$ nên điểm $O(0; 0)$ %s miền nghiệm của bất phương trình.'''       
                            % (a, val_b, val_b, cmp_b, c, res_b))

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
            if is_sol_c:
                vd_da_1_d = '\\True Miền nghiệm của bất phương trình là nửa mặt phẳng có bờ là đường thẳng $d: %s x - y = %s$, chứa điểm $A(%s; %s)$, kể cả bờ' % (a, c, xc, yc)
                vd_da_1_s = 'Miền nghiệm của bất phương trình là nửa mặt phẳng có bờ là đường thẳng $d: %s x - y = %s$, không chứa điểm $A(%s; %s)$, kể cả bờ' % (a, c, xc, yc)
            else:
                vd_da_1_d = '\\True Miền nghiệm của bất phương trình là nửa mặt phẳng có bờ là đường thẳng $d: %s x - y = %s$, không chứa điểm $A(%s; %s)$, kể cả bờ' % (a, c, xc, yc)
                vd_da_1_s = 'Miền nghiệm của bất phương trình là nửa mặt phẳng có bờ là đường thẳng $d: %s x - y = %s$, chứa điểm $A(%s; %s)$, kể cả bờ' % (a, c, xc, yc)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            cmp_c = "\\le" if is_sol_c else ">"
            res_c = "thuộc" if is_sol_c else "không thuộc"
            loigiai_vd_1 = ('''Thay tọa độ điểm $A(%s; %s)$ vào vế trái của bất phương trình ta có: \\\\
            $%s \\cdot (%s) - %s = %s$. \\\\
            Vì $%s %s %s$ nên điểm $A$ %s miền nghiệm của bất phương trình. \\\\
            Mặt khác, bất phương trình có chứa dấu "$\\le$" nên miền nghiệm kể cả đường thẳng bờ $d$.'''
                            % (xc, yc, a, xc, yc, val_c, val_c, cmp_c, c, res_c))

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
            wrong_num_m = num_m + 1 if num_m > 0 else 2
            vdc_da_1_d = '\\True Có $%s$ giá trị nguyên dương của $m$ để cặp số $(m; %s)$ là nghiệm của bất phương trình' % (num_m, yd)
            vdc_da_1_s = 'Có $%s$ giá trị nguyên dương của $m$ để cặp số $(m; %s)$ là nghiệm của bất phương trình' % (wrong_num_m, yd)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Để cặp số $(m; %s)$ là nghiệm của bất phương trình, ta phải có: \\\\
            $%s m - %s \\le %s \\Leftrightarrow %s m \\le %s \\Leftrightarrow m \\le %s$. \\\\
            Vì $m$ là số nguyên dương ($m \\in \\mathbb{Z}^+$) nên $m \\in \\{1; 2; ... ; %s\\}$ (nếu có). \\\\
            Vậy có $%s$ giá trị nguyên dương của $m$ thỏa mãn.'''
                             % (yd, a, yd, c, a, c + yd, str(round(max_m_exact, 2)).replace('.', ','), max_m_int, num_m))

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

