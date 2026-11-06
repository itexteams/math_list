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


def bt_dang22_p2_b1_c2_ds10(self):
            # Khai báo biến
            x, y = symbols('x y')

            # Khởi tạo ngẫu nhiên giao điểm trên các trục tọa độ (a > 0 trên Ox, b > 0 trên Oy)
            a = randint(2, 4)
            b = randint(2, 4)

            # Bất phương trình đường thẳng đi qua (a,0) và (0,b): b*x + a*y <= a*b
            gcd_val = math.gcd(b, math.gcd(a, a * b))
            a_simp = a // gcd_val
            b_simp = b // gcd_val
            c_simp = (a * b) // gcd_val

            ineq_lhs = b_simp * x + a_simp * y
            ineq_latex = '%s \\le %s' % (latex(ineq_lhs), latex(c_simp))
            ineq_s_latex = '%s \\ge %s' % (latex(ineq_lhs), latex(c_simp))

            # Diện tích tam giác
            area = Rational(a * b, 2)

            # Đếm số điểm tọa độ nguyên dương
            pts = [(xi, yi) for xi in range(1, a) for yi in range(1, b) if b * xi + a * yi <= a * b]
            num_points = len(pts)
            pts_str = ', '.join(['(%s;%s)' % (p[0], p[1]) for p in pts])

            # Tọa độ giao điểm bờ với các đường x = -1 và y = -1 (dùng float để TikZ vẽ không bị lỗi \frac)
            y_at_xmin = float(Rational(b * (a + 1), a))
            x_at_ymin = float(Rational(a * (b + 1), b))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Miền nghiệm của bất phương trình bậc nhất 2 ẩn là phần \\textbf{không} bị gạch trong hình vẽ sau: \\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt, >=stealth]
            \\draw[->] (-1,0) -- (%s,0) node[below]{$x$};
            \\draw[->] (0,-1) -- (0,%s) node[left]{$y$};
            \\draw (0,0) node[below right]{$O$};
            \\clip (-1,-1) rectangle (%s,%s);
            \\fill[pattern=north east lines] (-1,%s) -- (%s,-1) -- (%s,%s) -- (-1,%s) -- cycle;
            \\draw (-1,%s) -- (%s,-1);
            \\draw (0,%s) node[left]{$%s$};
            \\draw (%s,0) node[below]{$%s$};
            \\end{tikzpicture}
            \\end{center}''' %(
                latex(a + 2), latex(b + 2),
                latex(a + 2), latex(b + 2),
                y_at_xmin, x_at_ymin, latex(a + 2), latex(b + 2), latex(b + 2),
                y_at_xmin, x_at_ymin,
                latex(b), latex(b),
                latex(a), latex(a)
            ))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Mặt phẳng trên biểu diễn miền nghiệm của bất phương trình: $%s$' % ineq_latex
            nb_da_1_s = 'Mặt phẳng trên biểu diễn miền nghiệm của bất phương trình: $%s$' % ineq_s_latex
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Đường thẳng đi qua hai điểm $(%s; 0)$ và $(0; %s)$ có phương trình là $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s$. \\\\
            Thử điểm $O(0;0)$ vào bất phương trình $%s$, ta có $%s \\le %s$ (đúng) và điểm $O(0;0)$ thuộc miền không bị gạch. \\\\
            Do đó, mặt phẳng trên biểu diễn miền nghiệm của bất phương trình $%s$.'''
                %(latex(a), latex(b), latex(a), latex(b), latex(ineq_lhs) + '=' + latex(c_simp), ineq_latex, latex(0), latex(c_simp), ineq_latex)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Cặp số $(1;1)$ là $1$ nghiệm của bất phương trình trên'
            th_da_1_s = 'Cặp số $(%s;1)$ là $1$ nghiệm của bất phương trình trên' % latex(a)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thay $x = 1, y = 1$ vào bất phương trình $%s$, ta được: \\\\
            $%s \\cdot 1 + %s \\cdot 1 \\le %s \\Leftrightarrow %s \\le %s$ (mệnh đề đúng). \\\\
            Vậy cặp số $(1;1)$ là $1$ nghiệm của bất phương trình trên.'''
                %(ineq_latex, latex(b_simp), latex(a_simp), latex(c_simp), latex(b_simp + a_simp), latex(c_simp))
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Có %s điểm có tọa độ là số nguyên dương thuộc miền nghiệm của bất phương trình trên' % latex(num_points)
            vd_da_1_s = 'Có %s điểm có tọa độ là số nguyên dương thuộc miền nghiệm của bất phương trình trên' % latex(num_points + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            if num_points > 0:
                loigiai_vd_1 = ('''Các điểm có tọa độ là số nguyên dương ($x \\in \\mathbb{N}^*, y \\in \\mathbb{N}^*$) thuộc miền nghiệm thỏa mãn $%s$. \\\\
            Thử các giá trị nguyên dương ta tìm được các điểm là: $%s$. \\\\
            Vậy có tất cả %s điểm thỏa mãn.'''
                    %(ineq_latex, pts_str, latex(num_points))
                )
            else:
                loigiai_vd_1 = ('''Các điểm có tọa độ là số nguyên dương ($x \\in \\mathbb{N}^*, y \\in \\mathbb{N}^*$) thuộc miền nghiệm thỏa mãn $%s$. \\\\
            Do $x \\ge 1, y \\ge 1$ nên không có cặp số nguyên dương nào thỏa mãn bất phương trình. \\\\
            Vậy có $0$ điểm thỏa mãn.'''
                    %(ineq_latex)
                )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Bờ của miền nghiệm bất phương trình trên tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$' % latex(area)
            vdc_da_1_s = 'Bờ của miền nghiệm bất phương trình trên tạo với hai trục tọa độ một tam giác có diện tích bằng $%s$' % latex(a * b)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Bờ của miền nghiệm là đường thẳng $d$ cắt trục $Ox$ tại $A(%s;0)$ và cắt trục $Oy$ tại $B(0;%s)$. \\\\
            Tam giác $OAB$ vuông tại $O$ có $OA = %s$ và $OB = %s$. \\\\
            Diện tích tam giác $OAB$ là: $S = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.'''
                %(latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(area))
            )
            list_vdc_2 = [loigiai_vdc_1]

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

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

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
            str(noidungcauhoi) +
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

