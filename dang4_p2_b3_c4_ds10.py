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


def bt_dang4_p2_b3_c4_ds10(self):
            # Khai báo biến
            # ------------------------------------------------------------------------------------------------

            x = symbols('x')

            # Random hệ số b và c sao cho phương trình mẫu số có 2 nghiệm phân biệt (Delta > 0)
            while True:
                b_val = 2 * randint(-4, 4) # Chọn b chẵn để tính toán gọn hơn
                c_val = randint(-15, -1)   # Chọn c âm để đảm bảo a*c < 0 -> Delta luôn dương

                # Tạo biểu thức mẫu số: g(x) = x^2 + b_val*x + c_val
                g_x = x**2 + b_val*x + c_val

                # Tính nghiệm
                delta = b_val**2 - 4*c_val
                if delta > 0: # Đảm bảo có 2 nghiệm phân biệt
                    break

            # Lấy nghiệm và sắp xếp
            roots = solve(g_x, x)
            x1 = roots[0]
            x2 = roots[1]
            if x1 > x2:
                x1, x2 = x2, x1 # Đảm bảo x1 < x2

            # Tạo biểu thức f(x)
            f_expr_str = f"\\frac{{1}}{{{latex(g_x)}}}"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho biểu thức $f(x)=%s$.''' % (f_expr_str))

            # Hàm tạo code TikZ cho bảng xét dấu
            def create_tikz_table(x1_lat, x2_lat, sign_g, correct=True):
                # sign_g: dấu của tam thức bậc 2 (dương ở ngoài, âm ở trong)
                # correct: True vẽ bảng đúng, False vẽ bảng sai (ví dụ sai dấu f(x))

                # Logic bảng đúng:
                # x: -inf, x1, x2, +inf
                # g(x): +, 0, -, 0, +
                # f(x): +, ||, -, ||, +

                sign_mid = "-" if correct else "+"
                sign_out = "+" if correct else "-"

                tikz = ('''\\begin{tikzpicture}
            \\tkzTabInit[lgt=3,espcl=2.5]
            {$x$/0.8, $%s$/0.8, $f(x)$/0.8}
            {$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{,+,0,-,0,+,}
            \\tkzTabLine{,%s,||,%s,||,%s,}
            \\end{tikzpicture}''' % (latex(g_x), x1_lat, x2_lat, sign_out, sign_mid, sign_out))
                return tikz

            ######################################################################## Nhận biết (Câu a) ############################################
            # Nội dung: Kiểm tra phương trình f(x) = 0
            # Mệnh đề đúng: Vô nghiệm
            # Mệnh đề sai: Có nghiệm tại x1, x2 (nghiệm của mẫu)

            nb_da_1_d = '\\True $f(x)=0$ vô nghiệm'
            nb_da_1_s = '$f(x)=0 \\Leftrightarrow x=%s$ hoặc $x=%s$' % (latex(x1), latex(x2))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Lời giải a
            loigiai_nb_1 = ('''Ta có $f(x) = %s \\neq 0, \\forall x \\in \\mathscr{D}$. Do đó phương trình vô nghiệm.''' % (f_expr_str))
            list_nb_2 = [loigiai_nb_1]

            # Xử lý random
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu (Câu b) ############################################
            # Nội dung: Bảng xét dấu
            # Mệnh đề đúng: Bảng đúng logic
            # Mệnh đề sai: Bảng sai dấu của f(x)

            # Tạo bảng đúng
            tikz_true = create_tikz_table(latex(x1), latex(x2), sign_g=True, correct=True)
            # Tạo bảng sai (đảo dấu dòng cuối)
            tikz_false = create_tikz_table(latex(x1), latex(x2), sign_g=True, correct=False)

            th_da_1_d = '\\True Bảng xét dấu của biểu thức là: \\\\ \n ' + tikz_true
            th_da_1_s = 'Bảng xét dấu của biểu thức là: \\\\ \n ' + tikz_false

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Lời giải b
            loigiai_th_1 = ('''Mẫu số $%s$ có hai nghiệm phân biệt $x_1=%s, x_2=%s$. \\\\
            Ta có bảng xét dấu: \\\\ %s''' % (latex(g_x), latex(x1), latex(x2), tikz_true))
            list_th_2 = [loigiai_th_1]

            # Xử lý random
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng (Câu c) ############################################
            # Nội dung: Giải bất phương trình f(x) < 0
            # Mệnh đề đúng: x thuộc khoảng 2 nghiệm (x1; x2)
            # Mệnh đề sai: x thuộc hợp 2 khoảng ngoài (-inf; x1) U (x2; +inf)

            vd_da_1_d = '\\True Với $x \\in \\left(%s; %s\\right)$ thì $f(x) < 0$' % (latex(x1), latex(x2))
            vd_da_1_s = 'Với $x \\in \\left(-\\infty; %s\\right) \\cup \\left(%s; +\\infty\\right)$ thì $f(x) < 0$' % (latex(x1), latex(x2))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Lời giải c
            loigiai_vd_1 = ('''Dựa vào bảng xét dấu, ta thấy $f(x) < 0$ khi $x \\in \\left(%s; %s\\right)$.''' % (latex(x1), latex(x2)))
            list_vd_2 = [loigiai_vd_1]

            # Xử lý random
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao (Câu d) ############################################
            # Nội dung: Giải bất phương trình f(x) > 0
            # Mệnh đề đúng: x thuộc hợp 2 khoảng ngoài (-inf; x1) U (x2; +inf)
            # Mệnh đề sai: x thuộc khoảng trong (x1; x2)

            vdc_da_1_d = '\\True $f(x) > 0$ khi $x \\in \\left(-\\infty; %s\\right) \\cup \\left(%s; +\\infty\\right)$' % (latex(x1), latex(x2))
            vdc_da_1_s = '$f(x) > 0$ khi $x \\in \\left(%s; %s\\right)$' % (latex(x1), latex(x2))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Lời giải d
            loigiai_vdc_1 = ('''Dựa vào bảng xét dấu, ta thấy $f(x) > 0$ khi $x \\in \\left(-\\infty; %s\\right) \\cup \\left(%s; +\\infty\\right)$.''' % (latex(x1), latex(x2)))
            list_vdc_2 = [loigiai_vdc_1]

            # Xử lý random
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # ------------------------------------------------------------------------------------------------
            # LOGIC KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (Loop random lại nếu không thỏa mãn)
            # ------------------------------------------------------------------------------------------------

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chính để đảm bảo cấu trúc câu hỏi hợp lệ (có ít nhất 1 câu đúng, tối đa 3 câu đúng)
            # Lưu ý: Do code trên đã chạy logic random 1 lần rồi, để thực hiện vòng lặp while True bao trùm
            # toàn bộ việc chọn đáp án, ta cần đưa logic chọn list_nb_da_1... vào trong vòng lặp.
            # Dưới đây là đoạn code gom lại logic chọn lựa:

            while True:
                # Chọn ngẫu nhiên đáp án từ danh sách gốc
                nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
                th_da_1 = random.choice([th_da_1_d, th_da_1_s])
                vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                # Điều kiện dừng: Có từ 1 đến 3 ý đúng (tránh trường hợp toàn đúng hoặc toàn sai)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để chuẩn bị xuất
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # (Các biến lời giải list_nb_2... giữ nguyên vì nội dung lời giải đúng không thay đổi theo việc chọn đáp án sai/đúng)

            # Shuffle lần cuối (thực ra không cần thiết lắm vì ta đã chọn random ở trên, nhưng giữ đúng flow code mẫu)
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

