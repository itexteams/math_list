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


def bt_dang3_p2_b4_c1_hh11(self):
            # Khai báo biến
            hinhve=('''\\begin{center} \n'''
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'''
            '''\\clip(-1.457778299136516,-0.47822429313117554) rectangle (6.272832191454052,5.380255055687984);\n'''
            '''\\draw (0.,0.04)-- (3.,0.);\n'''
            '''\\draw (3.,0.)-- (5.,2.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (5.,2.)-- (2.,2.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,0.04);\n'''
            '''\\draw (0.,0.04)-- (0.,5.);\n'''
            '''\\draw (3.,0.)-- (3.,5.);\n'''
            '''\\draw (2.,4.)-- (0.,3.);\n'''
            '''\\draw (5.,4.)-- (3.,3.);\n'''
            '''\\draw (2.,4.)-- (5.,4.);\n'''
            '''\\draw (0.,3.)-- (3.,3.);\n'''
            '''\\draw (2.,4.)-- (3.,3.);\n'''
            '''\\draw (0.,3.)-- (5.,4.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (0.,0.04)-- (5.,2.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (3.,0.)-- (2.,2.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (2.,4.);\n'''
            '''\\draw [dash pattern=on 2pt off 2pt] (2.5,3.5)-- (2.488,1.024);\n'''
            '''\\draw (5.,2.)-- (5.,5.);\n'''
            '''\\draw (2.,4.)-- (2.,5.);\n'''
            '''\\draw (-0.5,0.3) node[anchor=north west] {$A$};\n'''
            '''\\draw (2.851351139251128,0.1834772311156166) node[anchor=north west] {$B$};\n'''
            '''\\draw (5.126958820197412,2.346111481092937) node[anchor=north west] {$C$};\n'''
            '''\\draw (-0.66,3.4435676676485922) node[anchor=north west] {$A'$};\n'''
            '''\\draw (3.157993309024032,3.330594236679628) node[anchor=north west] {$B'$};\n'''
            '''\\draw (5,4.395772300101293) node[anchor=north west] {$C'$};\n'''
            '''\\draw (1.35,4.557162915771243) node[anchor=north west] {$D'$};\n'''
            '''\\draw (2.0282589993343874,1) node[anchor=north west] {$O$};\n'''
            '''\\draw (2.36,4) node[anchor=north west] {$O'$};\n'''
            '''\\draw (1.4149746597885802,2.5236411583298812) node[anchor=north west] {$D$};\n'''
            '''\\end{tikzpicture}\n'''
            '''\\end{center}\n'''
                    )

            # Nội dung câu hỏi
            noidungcauhoi = '''Trong mặt phẳng $(P)$, cho hình bình hành $ABCD$ Vẽ các nửa đường thẳng song song nhau, nằm về một phía đối với mặt phẳng $(P)$ và đi qua các điểm $A,B,C,D$.'''
            ''' Một mặt phẳng $(Q)$ cắt bốn nửa đường thẳng nói trên tại $A',B',C',D'$ \n'''

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '''\\True mp$(AA',BB')$ song song mp$(CC',DD')$'''
            nb_da_1_s = '''mp$(AA',CC')$ song song mp$(BB',DD')$'''
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '''\\True mp$(AA',DD')$ song song mp$(BB',CC')$'''
            nb_da_2_s = '''mp$(ABCD)$ song song mp$(A'B'C'D')$'''
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Chứng minh mp$(AA',BB')$ song song mp$(CC',DD')$ \\\\ \n'''
                '''Ta có $AA'//DD'$ và $AB//CD$ nên $(AA',BB') // (CC',DD')$.'''
                        )
            loigiai_nb_2 = ('''Chứng minh mp$(AA',DD')$ song song mp$(BB',CC')$ \\\\ \n'''
                '''Ta có $AA'//BB'$ và $AD//BC$ nên $(AA',DD') // (BB',CC')$.'''
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '''\\True $A'B'//C'D'$'''
            th_da_1_s = '''$A'B'//AB$'''
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '''\\True $A'D'//B'C'$'''
            th_da_2_s = '''$A'C'//AC$'''
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('''Chứng minh $A'B'//C'D'$. \\\\ \n'''
                            '''Ta có $\\heva{& (AA',BB')//(CC',DD')\\\\& (Q)\\cap (AA',BB')=A'B'\\\\& (Q)\\cap (CC',DD')=C'D'} \\Rightarrow A'B'//C'D'$.'''
                                        )
            loigiai_th_2 = ('''Chứng minh $A'B'C'D'$ là hình bình hành. \\\\ \n'''
                            '''Ta có $\\heva{& (AA',DD')//(BB',CC')\\\\& (Q)\\cap (AA',DD')=A'D'\\\\& (Q)\\cap (BB',CC')=B'C'} \\Rightarrow A'D'//B'C'$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '''\\True $A'B'C'D'$ là hình bình hành'''
            vd_da_1_s = ''' $A'B'C'D'$ là hình thoi'''
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '''\\True $A'B'C'D'$ là hình bình hành'''
            vd_da_2_s = ''' $A'B'C'D'$ là hình hình thang cân'''
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Chứng minh $A'B'C'D'$ là hình bình hành. \\\\ \n'''
                            '''Ta có $\\heva{& (AA',BB')//(CC',DD')\\\\& (Q)\\cap (AA',BB')=A'B'\\\\& (Q)\\cap(CC',DD')=C'D'} \\Rightarrow A'B'//C'D'$   $(1)$.\\\\ \n'''
                            '''Tương tự $\\heva{& (AA',DD')//(BB',CC')\\\\& (Q)\\cap (AA',DD')=A'D'\\\\& (Q)\\cap(BB',CC')=B'C'} \\Rightarrow A'D'//B'C'$   $(2)$.\\\\ \n'''
                            '''Từ $(1)$ và $(2)$ $\\Rightarrow A'B'C'D'$ là hình bình hành.'''
                            )
            loigiai_vd_2 = ('''Chứng minh $A'B'C'D'$ là hình bình hành. \\\\ \n'''
                            '''Ta có $\\heva{& (AA',BB')//(CC',DD')\\\\& (Q)\\cap (AA',BB')=A'B'\\\\& (Q)\\cap(CC',DD')=C'D'} \\Rightarrow A'B'//C'D'$   $(1)$.\\\\ \n'''
                            '''Tương tự $\\heva{& (AA',DD')//(BB',CC')\\\\& (Q)\\cap (AA',DD')=A'D'\\\\& (Q)\\cap(BB',CC')=B'C'} \\Rightarrow A'D'//B'C'$   $(2)$.\\\\ \n'''
                            '''Từ $(1)$ và $(2)$ $\\Rightarrow A'B'C'D'$ là hình bình hành.'''
                            )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '''\\True Gọi $O$ và $O'$ lần lượt là giao điểm của hai đường chéo của $ABCD$ và $A'B'C'D'$. Khi đó $OO'//AA'$'''
            vdc_da_1_s = '''Gọi $O$ và $O'$ lần lượt là giao điểm của hai đường chéo của $ABCD$ và $A'B'C'D'$. Khi đó $AO//A'O'$'''
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '''\\True Gọi $O$ và $O'$ lần lượt là giao điểm của hai đường chéo của $ABCD$ và $A'B'C'D'$. Khi đó $OO'//BB'$'''
            vdc_da_2_s = '''Gọi $O$ và $O'$ lần lượt là giao điểm của hai đường chéo của $ABCD$ và $A'B'C'D'$. Khi đó $CO//CO'$'''
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\heva{& (ACC'A')//(BDD'B')=OO'\\\\& AA'\\subset (ACC'A');BB'\\subset (BDD'B') \\\\&AA'//BB'}$'''
                            ''' $\\Rightarrow OO'//AA'//BB'$ hay $OO'//AA'$.'''
                        )
            loigiai_vdc_2 = ('''Ta có $\\heva{& (ACC'A')//(BDD'B')=OO'\\\\& AA'\\subset (ACC'A');BB'\\subset (BDD'B') \\\\&AA'//BB'}$'''
                            ''' $\\Rightarrow OO'//AA'//BB'$ hay $OO'//BB'$.'''
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\loigiai{' +str(hinhve)+' \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

