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


def bt_dang24_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def fd(num):
                s = str(round(num, 5))
                if s.endswith('.0'): 
                    s = s[:-2]
                return s.replace('.', ',')

            # Random các xác suất P(A|B) và P(A|B_bar) sao cho ra số đẹp
            prob_pairs = [
                (0.4, 0.1),
                (0.6, 0.2),
                (0.3, 0.2),
                (0.2, 0.8),
                (0.8, 0.2),
                (0.5, 0.3),
                (0.7, 0.1)
            ]
            p1, p2 = random.choice(prob_pairs)

            # Random các thông số nhân sự
            N1 = random.choice([50, 60, 80, 100])
            N2 = random.choice([40, 50, 80, 100, 120])
            W1 = int(p1 * N1)
            W2 = int(p2 * N2)
            k = random.choice([2, 3, 4, 5])
            total_team = 2 * k

            # Tính toán các xác suất
            P_A = 0.5 * p1 + 0.5 * p2

            # Xử lý phân số cho P(B|A) để hiển thị số đẹp
            num_BA = sp.Rational(str(round(0.5 * p1, 4)))
            den_BA = sp.Rational(str(round(P_A, 4)))
            frac_BA = num_BA / den_BA
            P_B_given_A = float(frac_BA)

            # Hình vẽ sơ đồ cây bằng TikZ
            tikz_str = ('''\\begin{tikzpicture}[>=stealth, scale=1, thick]
            \\filldraw (0,0) circle (1pt);
            \\filldraw (2,1.5) circle (1pt) node[above left] {$B$} node[above right] {$0,5$};
            \\filldraw (2,-1.5) circle (1pt) node[below left] {$\\overline{B}$} node[below right] {$0,5$};
            \\draw[->] (0,0) -- (2,1.5);
            \\draw[->] (0,0) -- (2,-1.5);

            \\draw[->] (2,1.5) -- (4,2.5) node[above left] {$A$} node[right] {$%s$};
            \\draw[->] (2,1.5) -- (4,0.5) node[above left] {$\\overline{A}$} node[right] {$%s$};

            \\draw[->] (2,-1.5) -- (4,-0.5) node[above left] {$A$} node[right] {$%s$};
            \\draw[->] (2,-1.5) -- (4,-2.5) node[above left] {$\\overline{A}$} node[right] {$%s$};
            \\end{tikzpicture}''' % (fd(p1), fd(1-p1), fd(p2), fd(1-p2)))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty công nghệ có hai chi nhánh đặt tại Hà Nội và TP Hồ Chí Minh. Chi nhánh tại Hà Nội có $%s$ nhân viên, trong đó có $%s$ nhân viên nữ. Chi nhánh TP Hồ Chí Minh có $%s$ nhân viên, trong đó có $%s$ nhân viên nữ. Công ty quyết định thành lập một đội ngũ dịch vụ khách hàng gồm $%s$ người bằng cách chọn ngẫu nhiên từ mỗi chi nhánh $%s$ nhân viên và chọn ngẫu nhiên một nhân viên trong $%s$ nhân viên này để làm trưởng nhóm. Gọi $A$ là biến cố "Trưởng nhóm được chọn là nhân viên nữ" và $B$ là biến cố "Trưởng nhóm được chọn là nhân viên đến từ chi nhánh Hà Nội"''' 
                             % (N1, W1, N2, W2, total_team, k, total_team))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $P(B) = 0,5$'
            nb_da_1_s = '$P(B) = %s$' % random.choice(['0,25', '0,4', '0,6'])
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Cấu trúc lời giải cơ bản (chưa bao gồm đánh giá đúng sai)
            base_loigiai_nb_1 = ('''Mỗi chi nhánh chọn $%s$ nhân viên nên $P(B)=\\frac{%s}{%s}=\\frac{1}{2}=0,5$''' % (k, k, total_team))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $P(A|B) = %s$' % fd(p1)
            th_da_1_s = '$P(A|B) = %s$' % fd(round(p1 + random.choice([0.1, -0.1]), 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Xử lý hiển thị phân số rút gọn
            f_AB = sp.Rational(W1, N1)
            if f_AB.q != N1:
                th_sol_frac = "\\frac{%s}{%s}=\\frac{%s}{%s}=%s" % (W1, N1, f_AB.p, f_AB.q, fd(p1))
            else:
                th_sol_frac = "\\frac{%s}{%s}=%s" % (W1, N1, fd(p1))

            # Cấu trúc lời giải cơ bản
            base_loigiai_th_1 = ('''$P(A|B)=%s$''' % th_sol_frac)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $P(A) = %s$' % fd(P_A)
            vd_da_1_s = '$P(A) = %s$' % fd(round(P_A + random.choice([0.05, -0.05]), 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Cấu trúc lời giải cơ bản
            base_loigiai_vd_1 = ('''Ta có sơ đồ cây:\\\\
            \\begin{center}
            %s
            \\end{center}
            $P(A)=0,5 \\cdot %s + 0,5 \\cdot %s = %s$''' % (tikz_str, fd(p1), fd(p2), fd(P_A)))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $P(B|A) = %s$' % fd(P_B_given_A)
            vdc_da_1_s = '$P(B|A) = %s$' % fd(round(P_B_given_A + random.choice([0.1, -0.1]), 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Cấu trúc lời giải cơ bản
            if frac_BA.q != 1:
                vdc_sol_frac = "\\frac{%s}{%s}" % (frac_BA.p, frac_BA.q)
            else:
                vdc_sol_frac = "%s" % frac_BA.p

            base_loigiai_vdc_1 = ('''$P(B|A)=\\frac{0,5 \\cdot %s}{%s}=%s=%s$''' % (fd(p1), fd(P_A), vdc_sol_frac, fd(P_B_given_A)))

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

            # Sinh lời giải với kết luận đúng/sai linh hoạt tương ứng vào mệnh đề vừa được chọn
            loigiai_nb_1 = base_loigiai_nb_1 + (' nên mệnh đề này đúng.' if '\\True' in nb_da_1 else ' nên mệnh đề này sai.')
            loigiai_th_1 = base_loigiai_th_1 + (' nên mệnh đề này đúng.' if '\\True' in th_da_1 else ' nên mệnh đề này sai.')
            loigiai_vd_1 = base_loigiai_vd_1 + (' nên mệnh đề này đúng.' if '\\True' in vd_da_1 else ' nên mệnh đề này sai.')
            loigiai_vdc_1 = base_loigiai_vdc_1 + (' nên mệnh đề này đúng.' if '\\True' in vdc_da_1 else ' nên mệnh đề này sai.')

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

