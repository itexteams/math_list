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


def bt_dang13_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            a = randint(1, 5)
            b = randint(1, 4)
            if a == b:
                b += 1
            c = a * b

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $%sx + %sy \\ge %s$.'''
                             % (a, b, c))

            ########################################################################
            # Nhận biết ############################################
            x1 = randint(-2, 1)
            y1 = randint(-2, 1)
            val1 = a * x1 + b * y1
            is_sol = val1 >= c

            # Các đáp án
            if is_sol:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của bất phương trình trên' % (x1, y1)
                nb_da_1_s = 'Cặp số $(%s; %s)$ không là nghiệm của bất phương trình trên' % (x1, y1)
                loigiai_nb_1 = ('''Thay $x = %s, y = %s$ vào vế trái bất phương trình ta được: $%s \\cdot (%s) + %s \\cdot (%s) = %s \\ge %s$ (đúng). \\\\ 
                                Vậy cặp số $(%s; %s)$ là nghiệm của bất phương trình.''' 
                                % (x1, y1, a, x1, b, y1, val1, c, x1, y1))
            else:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ không là nghiệm của bất phương trình trên' % (x1, y1)
                nb_da_1_s = 'Cặp số $(%s; %s)$ là nghiệm của bất phương trình trên' % (x1, y1)
                loigiai_nb_1 = ('''Thay $x = %s, y = %s$ vào vế trái bất phương trình ta được: $%s \\cdot (%s) + %s \\cdot (%s) = %s < %s$ (sai). \\\\ 
                                Vậy cặp số $(%s; %s)$ không là nghiệm của bất phương trình.''' 
                                % (x1, y1, a, x1, b, y1, val1, c, x1, y1))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

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
            th_da_1_d = '\\True Những điểm nằm trên đường thẳng $%sx + %sy = %s$ thuộc miền nghiệm của bất phương trình' % (a, b, c)
            th_da_1_s = 'Những điểm nằm trên đường thẳng $%sx + %sy = %s$ không thuộc miền nghiệm của bất phương trình' % (a, b, c)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Do bất phương trình chứa dấu $\\ge$ nên miền nghiệm của bất phương trình lấy cả bờ là đường thẳng $%sx + %sy = %s$. \\\\
                            Do đó những điểm nằm trên đường thẳng này thuộc miền nghiệm của bất phương trình.''' 
                            % (a, b, c))

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
            y_at_x_minus_1_5 = round((c + 1.5 * a) / b, 2)
            x_at_y_minus_1_5 = round((c + 1.5 * b) / a, 2)
            xmax = b + 1.5
            ymax = a + 1.5

            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]
            \\draw[->] (-1.5,0) -- (%s,0) node[above] {$x$};
            \\draw[->] (0,-1.5) -- (0,%s) node[right] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\clip (-1.5,-1.5) rectangle (%s,%s);
            \\fill[pattern=north east lines, pattern color=black!60] (-1.5, %s) -- (%s, -1.5) -- (-1.5,-1.5) -- cycle;
            \\draw (-1.5, %s) -- (%s, -1.5);
            \\filldraw[black] (%s,0) circle (0pt) node[above right] {$%s$};
            \\filldraw[black] (0,%s) circle (0pt) node[above right] {$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (xmax, ymax, xmax, ymax, y_at_x_minus_1_5, x_at_y_minus_1_5, y_at_x_minus_1_5, x_at_y_minus_1_5, b, b, a, a))

            # Các đáp án
            vd_da_1_d = '\\True Miền nghiệm của bất phương trình trên là phần không bị gạch kể cả đường thẳng $%sx + %sy = %s$ %s' % (a, b, c, tikz_code)
            vd_da_1_s = 'Miền nghiệm của bất phương trình trên là phần bị gạch kể cả đường thẳng $%sx + %sy = %s$ %s' % (a, b, c, tikz_code)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét điểm $O(0;0)$. Thay $x=0, y=0$ vào bất phương trình ta được $0 \\ge %s$ (vô lý). \\\\
                            Do đó miền nghiệm không chứa gốc tọa độ $O$. Trên hình vẽ, phần mặt phẳng chứa $O$ đã bị gạch bỏ. \\\\
                            Vậy miền nghiệm là phần không bị gạch, kể cả bờ.''' 
                            % (c))

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
            distance = sp.simplify(sp.Rational(c, 1) / sp.sqrt(a**2 + b**2))
            latex_d = sp.latex(distance)
            distance_false = sp.simplify(sp.Rational(c + 2, 1) / sp.sqrt(a**2 + b**2))
            latex_d_false = sp.latex(distance_false)

            # Các đáp án
            vdc_da_1_d = '\\True Điểm $M(x_0; y_0)$ thuộc miền nghiệm của bất phương trình trên. Độ dài nhỏ nhất của $OM$ bằng $%s$' % (latex_d)
            vdc_da_1_s = 'Điểm $M(x_0; y_0)$ thuộc miền nghiệm của bất phương trình trên. Độ dài nhỏ nhất của $OM$ bằng $%s$' % (latex_d_false)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Điểm $M$ thuộc miền nghiệm của bất phương trình, tức là $M$ nằm trong nửa mặt phẳng không chứa $O$, có bờ là đường thẳng $\\Delta: %sx + %sy - %s = 0$. \\\\
                            Để đoạn thẳng $OM$ có độ dài nhỏ nhất thì $M$ phải là hình chiếu vuông góc của $O$ lên đường thẳng $\\Delta$. \\\\
                            Khi đó khoảng cách nhỏ nhất là $OM = d(O, \\Delta) = \\frac{|%s \\cdot 0 + %s \\cdot 0 - %s|}{\\sqrt{%s^2 + %s^2}} = %s$.''' 
                            % (a, b, c, a, b, c, a, b, latex_d))

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
                ' \\choiceTFn \n'
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

