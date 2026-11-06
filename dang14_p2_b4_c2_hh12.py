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


def bt_dang14_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            x_I = random.randint(1, 5)
            y_I = random.randint(1, 5)
            z_I = 12

            # Các điểm được xây dựng tương đối theo I để đảm bảo nghiệm luôn đẹp
            M_x = x_I + 1
            M_y = y_I
            N_x = x_I + 6
            N_y = y_I + 8
            A_x = x_I + 4
            A_y = y_I + 8
            B_x = x_I - 6

            b_val = Rational(2*y_I + 1, 2)
            b_val_f = Rational(2*y_I + 3, 2)
            b_true_tex = latex(b_val)
            b_false_tex = latex(b_val_f)

            C_val = 4*A_y - 3*A_x
            C_val_B = 3*B_x + C_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, một trạm thu phát sóng điện thoại di động được đặt ở vị trí $I(%s;%s;%s)$, trong đó một đơn vị độ dài trên mỗi trục tương ứng với $10$ mét trên thực tế. Trạm thu phát sóng đó có bán kính phủ sóng là $130$ mét. Vùng phủ sóng của trạm thu phát được quy ước là tập hợp tất cả các điểm $P$ trên mặt đất và trong không gian sao cho khoảng cách $IP$ không vượt quá $130$ mét. Mặt đất được coi là một phần của mặt phẳng $(Oxy)$ và mỗi người trên mặt đất được coi như một chất điểm.'''                 
                             % (x_I, y_I, z_I))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vùng phủ sóng của trạm thu phát là một phần của hình cầu giới hạn bởi mặt cầu $(S)$ có phương trình $(x-%s)^2+(y-%s)^2+(z-%s)^2=169$' % (x_I, y_I, z_I)
            nb_da_1_s = 'Vùng phủ sóng của trạm thu phát là một phần của hình cầu giới hạn bởi mặt cầu $(S)$ có phương trình $(x-%s)^2+(y-%s)^2+(z-%s)^2=130$' % (x_I, y_I, z_I)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Bán kính mặt cầu là $R = \\frac{130}{10} = 13$.\\\\
            Mặt cầu $(S)$ tâm $I(%s;%s;%s)$ và bán kính $R=13$ có phương trình là $(x-%s)^2+(y-%s)^2+(z-%s)^2=169$.'''
                            % (x_I, y_I, z_I, x_I, y_I, z_I))

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
            th_da_1_d = '\\True Giả sử một người cầm điện thoại đang ở vị trí điểm $M(%s;%s;0)$ và chuyển động thẳng đều trên mặt đất với tốc độ $3{,}6 \\text{ km/h}$. Khi đó, tại giây thứ 70 tính từ lúc xuất phát ở vị trí điểm $M(%s;%s;0)$, người đó đã đi được ra ngoài vùng phủ sóng của trạm thu phát' % (M_x, M_y, M_x, M_y)  
            th_da_1_s = 'Giả sử một người cầm điện thoại đang ở vị trí điểm $M(%s;%s;0)$ và chuyển động thẳng đều trên mặt đất với tốc độ $3{,}6 \\text{ km/h}$. Khi đó, tại giây thứ 40 tính từ lúc xuất phát ở vị trí điểm $M(%s;%s;0)$, người đó đã đi được ra ngoài vùng phủ sóng của trạm thu phát' % (M_x, M_y, M_x, M_y)   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vùng phủ sóng trên mặt đất là hình tròn $(C)$ tâm $I'(%s;%s;0)$ bán kính $r = \\sqrt{R^2 - z_I^2} = \\sqrt{13^2 - 12^2} = 5$ (đơn vị), tương ứng với $50\\text{ m}$.\\\\
            Khoảng cách ban đầu từ $M$ đến tâm $I'$ là $I'M = \\sqrt{(%s-%s)^2 + (%s-%s)^2} = 1$ (đơn vị), tương ứng với $10\\text{ m}$.\\\\
            Tốc độ $v = 3{,}6 \\text{ km/h} = 1 \\text{ m/s}$.\\\\
            Nếu đi trong 40 giây, quãng đường là $40\\text{ m}$. Khoảng cách xa nhất đến $I'$ có thể là $10 + 40 = 50\\text{ m} \\le 50\\text{ m}$, nên người đó vẫn luôn nằm trong (hoặc trên biên) vùng phủ sóng (Phát biểu giây thứ 40 là sai).\\\\
            Nếu đi trong 70 giây, quãng đường là $70\\text{ m}$. Khoảng cách gần nhất đến $I'$ là $|70 - 10| = 60\\text{ m} > 50\\text{ m}$, nên người đó chắc chắn đã ra ngoài vùng phủ sóng (Phát biểu giây thứ 70 là đúng).'''       
                            % (x_I, y_I, M_x, x_I, M_y, y_I))

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
            vd_da_1_d = '\\True Khoảng cách ngắn nhất để một người cầm điện thoại đang ở vị trí có tọa độ $N(%s;%s;0)$ di chuyển trên mặt đất tới được vùng phủ sóng (theo đơn vị mét) là $50\\text{ m}$' % (N_x, N_y)  
            vd_da_1_s = 'Khoảng cách ngắn nhất để một người cầm điện thoại đang ở vị trí có tọa độ $N(%s;%s;0)$ di chuyển trên mặt đất tới được vùng phủ sóng (theo đơn vị mét) là $100\\text{ m}$' % (N_x, N_y)  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Khoảng cách từ $N(%s;%s;0)$ đến tâm $I'(%s;%s;0)$ của vùng phủ sóng trên mặt đất là $I'N = \\sqrt{(%s-%s)^2 + (%s-%s)^2} = 10$ (đơn vị).\\\\
            Khoảng cách ngắn nhất tới vùng phủ sóng là $(I'N - r) \\cdot 10 = (10 - 5) \\cdot 10 = 50\\text{ m}$.'''  
                            % (N_x, N_y, x_I, y_I, N_x, x_I, N_y, y_I))

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
            vdc_da_1_d = '\\True Giả sử một người cầm điện thoại chuyển động thẳng đều trên mặt đất từ vị trí $A(%s;%s;0)$ đến vị trí $B(%s;b;0)$ với tốc độ $3{,}6 \\text{ km/h}$ sao cho khoảng thời gian người đó thuộc vùng phủ sóng đúng bằng $60$ giây. Khi đó $b=%s$' % (A_x, A_y, B_x, b_true_tex) 
            vdc_da_1_s = 'Giả sử một người cầm điện thoại chuyển động thẳng đều trên mặt đất từ vị trí $A(%s;%s;0)$ đến vị trí $B(%s;b;0)$ với tốc độ $3{,}6 \\text{ km/h}$ sao cho khoảng thời gian người đó thuộc vùng phủ sóng đúng bằng $60$ giây. Khi đó $b=%s$' % (A_x, A_y, B_x, b_false_tex) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Quãng đường người đó di chuyển trong vùng phủ sóng (hình tròn tâm $I'(%s;%s)$, bán kính $r=5$) là $60 \\cdot 1 = 60\\text{ m} = 6$ (đơn vị).\\\\
            Khoảng cách từ tâm $I'$ đến đường thẳng $AB$ là $h = \\sqrt{r^2 - \\left(\\frac{6}{2}\\right)^2} = \\sqrt{25 - 9} = 4$.\\\\
            Đường thẳng $AB$ đi qua $A(%s;%s)$. Gọi phương trình $AB$ có dạng $c(x-%s) + d(y-%s) = 0$ ($c^2+d^2 > 0$).\\\\
            $d(I', AB) = 4 \\Leftrightarrow \\frac{|c(%s-%s) + d(%s-%s)|}{\\sqrt{c^2+d^2}} = 4 \\Leftrightarrow \\frac{|-4c - 8d|}{\\sqrt{c^2+d^2}} = 4 \\Leftrightarrow |-c - 2d| = \\sqrt{c^2+d^2}$.\\\\
            Bình phương hai vế ta được $c^2 + 4cd + 4d^2 = c^2 + d^2 \\Leftrightarrow 3d^2 + 4cd = 0 \\Leftrightarrow d(3d + 4c) = 0$.\\\\
            Trường hợp 1: $d=0 \\Rightarrow c \\neq 0$. Phương trình $AB$: $x=%s$. Thay $B(%s;b)$ vào ta được $%s=%s$ (vô lý).\\\\
            Trường hợp 2: $3d+4c=0$. Chọn $c=3, d=-4$, phương trình $AB$: $3(x-%s) - 4(y-%s) = 0 \\Leftrightarrow 3x - 4y + %s = 0$.\\\\
            Điểm $B(%s;b) \\in AB \\Rightarrow 3(%s) - 4b + %s = 0 \\Leftrightarrow 4b = %s \\Leftrightarrow b = %s$.'''
                            % (x_I, y_I, A_x, A_y, A_x, A_y, x_I, A_x, y_I, A_y, A_x, B_x, B_x, A_x, A_x, A_y, C_val, B_x, B_x, C_val, C_val_B, b_true_tex))

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
                str(noidungcauhoi)+ '\n'
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

