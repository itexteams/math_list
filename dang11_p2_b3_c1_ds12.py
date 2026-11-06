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


def bt_dang11_p2_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên cho bài toán
            x_1 = random.randint(-5, -1)
            x_2 = random.randint(x_1 + 1, x_1 + 4)
            x_3 = random.randint(x_2 + 1, x_2 + 4)

            y_1 = random.randint(1, 5)
            y_2 = random.randint(y_1 + 1, y_1 + 5)
            y_3 = random.randint(y_2 + 1, y_2 + 6)
            y_4 = random.randint(-2, y_3 - 1)
            while y_4==y_1:
                x_1 = random.randint(-5, -1)
                x_2 = random.randint(x_1 + 1, x_1 + 4)
                x_3 = random.randint(x_2 + 1, x_2 + 4)

                y_1 = random.randint(1, 5)
                y_2 = random.randint(y_1 + 1, y_1 + 5)
                y_3 = random.randint(y_2 + 1, y_2 + 6)
                y_4 = random.randint(-2, y_3 - 1)    

            # Nội dung câu hỏi - Đã cấu hình double distance=2pt để hai nét song song đều nhau tuyệt đối
            noidungcauhoi = ('''Cho hàm số $y=f(x)$ xác định và liên tục trên $\\mathbb{R} \\setminus \\{%s; %s\\}$ và có bảng biến thiên như hình sau: \\\\
            \\begin{center}
            \\begin{tikzpicture}[line width=0.5pt, double distance=2pt]
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/0.7,$y\'$/0.7,$y$/2.1}
            {$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,d,+,d,+,0,-,}
            \\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+D-/$%s$/$-\\infty$,+/$%s$,-/$%s$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x_1), latex(x_2), latex(x_1), latex(x_2), latex(x_3), latex(y_1), latex(y_2), latex(y_3), latex(y_4)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đồ thị hàm số có hai đường tiệm cận đứng là $x=%s$ và $x=%s$' % (latex(x_1), latex(x_2))
            nb_da_1_s = 'Đồ thị hàm số có ba đường tiệm cận đứng'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào bảng biến thiên, ta thấy: \\\\
            - Do $\\lim_{x \\to %s^-} f(x) = +\\infty$ nên đường thẳng $x=%s$ là một đường tiệm cận đứng của đồ thị hàm số. \\\\
            - Do $\\lim_{x \\to %s^+} f(x) = -\\infty$ nên đường thẳng $x=%s$ là một đường tiệm cận đứng của đồ thị hàm số. \\\\
            Vậy đồ thị hàm số đã cho có hai đường tiệm cận đứng.''' % (latex(x_1), latex(x_1), latex(x_2), latex(x_2)))

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
            th_da_1_d = '\\True Đồ thị hàm số có hai đường tiệm cận ngang là $y=%s$ và $y=%s$' % (latex(y_1), latex(y_4))
            th_da_1_s = 'Đồ thị hàm số có đúng một đường tiệm cận ngang'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Dựa vào bảng biến thiên, ta thấy: \\\\
            - Do $\\lim_{x \\to -\\infty} f(x) = %s$ nên đường thẳng $y=%s$ là một đường tiệm cận ngang của đồ thị hàm số. \\\\
            - Do $\\lim_{x \\to +\\infty} f(x) = %s$ nên đường thẳng $y=%s$ là một đường tiệm cận ngang của đồ thị hàm số. \\\\
            Vì $%s \\neq %s$ nên đồ thị hàm số có hai đường tiệm cận ngang phân biệt.''' % (latex(y_1), latex(y_1), latex(y_4), latex(y_4), latex(y_1), latex(y_4)))

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
            vd_da_1_d = '\\True Hàm số đồng biến trên khoảng $\\left(-\\infty; %s\\right)$' % (latex(x_1))
            vd_da_1_s = 'Hàm số đồng biến trên khoảng $\\left(-\\infty; %s\\right)$' % (latex(x_2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dựa vào bảng biến thiên, trên khoảng $\\left(-\\infty; %s\\right)$ ta thấy đạo hàm $y\' > 0$ nên hàm số đồng biến trên khoảng đó. Hàm số không đồng biến trên khoảng $\\left(-\\infty; %s\\right)$ vì chứa điểm gián đoạn $x=%s$.''' % (latex(x_1), latex(x_2), latex(x_1)))

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
            vdc_da_1_d = '\\True Đồ thị hàm số có điểm cực đại là $\\left(%s; %s\\right)$' % (latex(x_3), latex(y_3))
            vdc_da_1_s = 'Đồ thị hàm số đạt cực đại tại $x=%s$' % (latex(x_2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Dựa vào bảng biến thiên, đạo hàm $y\'$ đổi dấu từ dương sang âm khi đi qua điểm $x=%s$ và hàm số xác định tại đây. Do đó, hàm số đạt cực đại tại $x=%s$ và giá trị cực đại tương ứng là $y=%s$. Suy ra điểm cực đại của đồ thị hàm số là $\\left(%s; %s\\right)$.''' % (latex(x_3), latex(x_3), latex(y_3), latex(x_3), latex(y_3)))

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
                '\\choiceTFn \n'
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

