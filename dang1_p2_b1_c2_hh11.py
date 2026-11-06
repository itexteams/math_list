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


def bt_dang1_p2_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                sa=2*a
                ab=a
                ad=3*a
                ia=Rational(sa,2)
                ib=sqrt(ia**2+ab**2)
                bd=sqrt(ab**2+ad**2)
                oa=bd/2 
                oi=sqrt(ia**2+oa**2)
                giatri=(oi**2+oa**2-ib**2)/(2*oi*oa)

                goc1=acos(giatri)
                gocz=goc1*180/pi

                h1=gocz 
                number = Decimal(float(h1))  # Số cần làm tròn
                goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $SzzABCD$ có đáy $ABCD$ là hình chữ nhật, các tam giác $SAB$, $SAD$, $SAC$ là các giác vuông tại $A$zz Biết $SA=%s$, $AB=%s$, $AD=%s$zz
                                '''
                                %(latex(sa),latex(ab), latex(ad)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $IB=%s$' %(latex(ib))
                nb_da_1_s = '$IB=%s$' %(latex(sqrt(ia**2+ab**2-1)))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = (
                    '''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-4zz18,-2zz82) rectangle (5zz96,4zz78);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (-3zz,-2zz);
                    \\draw [line width=1zzpt] (-3zz,-2zz)-- (2zz,-2zz);
                    \\draw [line width=1zzpt] (2zz,-2zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (0zz,4zz);
                    \\draw [line width=1zzpt] (0zz,4zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,4zz)-- (-3zz,-2zz);
                    \\draw [line width=1zzpt] (0zz,4zz)-- (2zz,-2zz);
                    \\draw (-0zz2,4zz6) node[anchor=north west] {$S$};
                    \\draw (-0zz6,0zz66) node[anchor=north west] {$A$};
                    \\draw (-3zz56,-1zz8) node[anchor=north west] {$B$};
                    \\draw (1zz98,-1zz86) node[anchor=north west] {$C$};
                    \\draw (5zz08,0zz48) node[anchor=north west] {$D$};
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (-3zz,-2zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (2zz,-2zz)-- (0zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,2zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,2zz)-- (-3zz,-2zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,2zz)-- (1zz,-1zz);
                    \\draw (0zz64,-1) node[anchor=north west] {$O$};
                    \\draw (-0zz48,2zz6) node[anchor=north west] {$I$};
                \\end{tikzpicture}
            \\end{center}
            Gọi $O$ là tâm của hình chữ nhật $ABCD$, $I$ là trung điểm của $SA$zz \\\\
            Trong $\\triangle SAC$ có $OI//SC$ suy ra $\\left(SC,BD\\right)=\\left(OI,BD\\right)=\\hoac{ &\\widehat{IOB}\\\\ &180^\\circ-\\widehat{IOB}}$zz \\\\
            Áp dụng định lý Pitago cho tam giác vuông $ABI$ có: \\\\
            $IB=\\sqrt{IA^2+AB^2}=\\sqrt{%s^2+%s^2}=%s$zz'''
            %(latex(ia),latex(ab),latex(ib)))

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
                th_da_1_d = '\\True $OB=%s$' %(latex(oa))  
                th_da_1_s = '$OB=%s$' %(latex(sqrt(ab**2+ad**2)/3))   
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = (
                    '''
                    Ta có $ABCD$ là hình chữ nhật nên $BD=\\sqrt{AB^2+AD^2}=\\sqrt{{%s^2}+{%s^2}}=%s$zz
                    suy ra $OB=OA=\\dfrac{BD}{2}=%s$zz
                    '''
                        %(latex(ab),latex(ad),latex(bd),
                        latex(oa)))

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
                vd_da_1_d = '\\True $OI=%s$' %(latex(oi))  
                vd_da_1_s = '$OI=%s$' %(latex(sqrt(ia**2+oa**2+1))) 
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                    '''
                    Áp dụng định lý Pitago cho tam giác vuông $ABO$ ta có \\\\
                    $OI=\\sqrt{IA^2+OA^2}=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2}=%s$zz
                    '''
                            %(latex(ia),latex(oa),latex(oi),))

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
                vdc_da_1_d = '\\True $\\left(SC,BD\\right)=%s^\\circ$' %(latex(goc)) 
                vdc_da_1_s = '$\\left(SC,BD\\right)=%s^\\circ$' %(latex(goc+1)) 
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                    '''
                    Khi đó, theo định lý hàm số cosin cho $\\triangle IOB$ ta được: \\\\
                    $\\cos \\widehat{IOB}=\\dfrac{OI^2+OB^2-IB^2}{2\\cdot OI \\cdot OB}=\\dfrac{%s+%s-%s}{2 \\cdot %s \\cdot %s}=%s$zz \\\\
                    Suy ra $\\left(SC,BD\\right)=\\widehat{IOB}=%s^\\circ$zz \\\\
                    Vậy $\\left(SC,BD\\right)=%s^\\circ$zz
                    '''
                            %(latex(oi**2),latex(oa**2),latex(ib**2),latex(oi),latex(oa),latex(giatri),
                            latex(goc),latex(goc)))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

