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


def bt_dang18_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random số liệu bài toán
            m_bo = random.choice([200, 226, 250])
            p_bo = random.choice([50, 59, 60])
            m_trung = random.choice([40, 46, 50])
            p_trung = random.choice([5, 6, 7])
            limit = random.choice([50, 60, 70])

            frac_bo = Rational(p_bo, m_bo)
            frac_trung = Rational(p_trung, m_trung)

            # Số liệu cho câu c
            x0 = 150
            y0 = 2 * m_trung
            val_c = frac_bo * x0 + frac_trung * y0
            is_sol_c = (val_c <= limit)

            # Số liệu cho câu d
            x1 = 200
            num_eggs = 2
            y1 = num_eggs * m_trung
            val_d = frac_bo * x1 + frac_trung * y1
            is_suitable_d = (val_d <= limit)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho biết $%s\\text{ g}$ thịt bò chứa khoảng $%s\\text{ g}$ protein. Một quả trứng nặng $%s\\text{ g}$ có chứa khoảng $%s\\text{ g}$ protein. Giả sử có một người mỗi ngày cần không quá $%s\\text{ g}$ protein. Gọi số gam thịt bò và số gam trứng mà người đó ăn trong một ngày lần lượt là $x, y$.''' 
                             % (m_bo, p_bo, m_trung, p_trung, limit))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số gam protein từ thịt bò là $%s x$; số gam protein từ trứng là $%s y$' % (latex(frac_bo), latex(frac_trung))
            nb_da_1_s = 'Số gam protein từ thịt bò là $%s x$; số gam protein từ trứng là $%s y$' % (latex(frac_trung), latex(frac_bo))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $%s\\text{ g}$ thịt bò chứa $%s\\text{ g}$ protein nên $1\\text{ g}$ thịt bò chứa $\\frac{%s}{%s}\\text{ g}$ protein. Do đó $x\\text{ g}$ thịt bò chứa $%s x\\text{ g}$ protein. \\\\
            Một quả trứng nặng $%s\\text{ g}$ chứa $%s\\text{ g}$ protein nên $1\\text{ g}$ trứng chứa $\\frac{%s}{%s}\\text{ g}$ protein. Do đó $y\\text{ g}$ trứng chứa $%s y\\text{ g}$ protein.'''
                            % (m_bo, p_bo, p_bo, m_bo, latex(frac_bo), m_trung, p_trung, p_trung, m_trung, latex(frac_trung)))

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
            th_da_1_d = '\\True Bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày là $%s x + %s y \\le %s$' % (latex(frac_bo), latex(frac_trung), limit)  
            th_da_1_s = 'Bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày là $%s x + %s y \\ge %s$' % (latex(frac_bo), latex(frac_trung), limit)   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tổng số gam protein từ thịt bò và trứng ăn trong một ngày là $%s x + %s y$. \\\\
            Vì nhu cầu mỗi ngày cần không quá $%s\\text{ g}$ protein nên ta có bất phương trình $%s x + %s y \\le %s$.'''       
                            % (latex(frac_bo), latex(frac_trung), limit, latex(frac_bo), latex(frac_trung), limit))

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
            val_c_str = str(round(float(val_c), 2)).replace('.', ',')
            if is_sol_c:
                vd_da_1_d = '\\True Cặp số (%s; %s) là một nghiệm của bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày' % (x0, y0)
                vd_da_1_s = 'Cặp số (%s; %s) không là nghiệm của bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày' % (x0, y0)
            else:
                vd_da_1_d = '\\True Cặp số (%s; %s) không là nghiệm của bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày' % (x0, y0)
                vd_da_1_s = 'Cặp số (%s; %s) là một nghiệm của bất phương trình theo $x, y$ diễn tả giới hạn về lượng protein mà người đó cần mỗi ngày' % (x0, y0)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            cmp_str_c = "\\le" if is_sol_c else ">"
            sol_text_c = "là một nghiệm" if is_sol_c else "không là nghiệm"
            loigiai_vd_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của bất phương trình $%s x + %s y \\le %s$, ta được: \\\\
            $%s \\cdot %s + %s \\cdot %s \\approx %s %s %s$. \\\\
            Do đó cặp số $(%s; %s)$ %s của bất phương trình.'''
                            % (x0, y0, latex(frac_bo), latex(frac_trung), limit,
                               latex(frac_bo), x0, latex(frac_trung), y0, val_c_str, cmp_str_c, limit,
                               x0, y0, sol_text_c))

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
            val_d_str = str(round(float(val_d), 2)).replace('.', ',')
            if is_suitable_d:
                vdc_da_1_d = '\\True Nếu người đó ăn %s\\text{ g} thịt bò và %s quả trứng, mỗi quả %s\\text{ g}, trong một ngày thì phù hợp' % (x1, num_eggs, m_trung)
                vdc_da_1_s = 'Nếu người đó ăn %s\\text{ g} thịt bò và %s quả trứng, mỗi quả %s\\text{ g}, trong một ngày thì không phù hợp' % (x1, num_eggs, m_trung)
            else:
                vdc_da_1_d = '\\True Nếu người đó ăn %s\\text{ g} thịt bò và %s quả trứng, mỗi quả %s\\text{ g}, trong một ngày thì không phù hợp' % (x1, num_eggs, m_trung)
                vdc_da_1_s = 'Nếu người đó ăn %s\\text{ g} thịt bò và %s quả trứng, mỗi quả %s\\text{ g}, trong một ngày thì phù hợp' % (x1, num_eggs, m_trung)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            cmp_str_d = "\\le" if is_suitable_d else ">"
            suit_text_d = "phù hợp" if is_suitable_d else "không phù hợp"
            loigiai_vdc_1 = ('''Khối lượng trứng ăn trong một ngày là $y = %s \\cdot %s = %s\\text{ g}$. \\\\
            Khối lượng thịt bò ăn trong một ngày là $x = %s\\text{ g}$. \\\\
            Thay $x = %s$ và $y = %s$ vào biểu thức vế trái bất phương trình $%s x + %s y \\le %s$, ta có: \\\\
            $%s \\cdot %s + %s \\cdot %s \\approx %s %s %s$. \\\\
            Vậy khẩu phần ăn này %s với nhu cầu protein mỗi ngày.'''
                             % (num_eggs, m_trung, y1, x1, x1, y1, latex(frac_bo), latex(frac_trung), limit,
                                latex(frac_bo), x1, latex(frac_trung), y1, val_d_str, cmp_str_d, limit, suit_text_d))

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

